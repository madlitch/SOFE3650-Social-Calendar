from database import database
from models import *
from sqlalchemy import or_, func
from sqlalchemy.sql import select, insert, desc
from exceptions import *
import auth
import tables
import models
import asyncpg
import uuid
import json


# User ---------------------------------------------------


async def create_user(user: UserIn):
    user.username = user.username.lower()
    if len(user.username) < 3 or len(user.username) > 20:
        raise API_406_USERNAME_EXCEPTION
    query = tables.users.select().where(tables.users.c.username == user.username)
    existing_user = await database.execute(query)
    if existing_user:
        raise API_409_USERNAME_CONFLICT_EXCEPTION
    elif len(user.password) < 4:
        raise API_406_PASSWORD_EXCEPTION
    else:
        salt = auth.gen_salt()
        query = tables.users.insert().values(username=user.username,
                                             first_name=user.first_name,
                                             last_name=user.last_name,
                                             hashed_password=auth.get_password_hash(user.password + salt), salt=salt)
        user_id = await database.execute(query)
        return {**user.dict(), "user_id": user_id}


# Friends ---------------------------------------------------


async def get_friends(user: User):
    query = select([tables.friends.join(tables.users, tables.friends.c.user_id_1 == tables.users.c.user_id)])\
        .where(or_(tables.friends.c.user_id_1 == user.user_id, tables.friends.c.user_id_2 == user.user_id))\
        .where(tables.users.c.user_id != user.user_id)\
        .union(
        select([tables.friends.join(tables.users, tables.friends.c.user_id_2 == tables.users.c.user_id)])
        .where(or_(tables.friends.c.user_id_1 == user.user_id, tables.friends.c.user_id_2 == user.user_id))
        .where(tables.users.c.user_id != user.user_id))
    return await database.fetch_all(query)


async def create_friend_relationship(friend: NewFriend, user: User):
    query = select([tables.users.c.user_id]).where(tables.users.c.username == friend.username.lower())
    friend_id = await database.execute(query)
    if friend_id:
        if friend_id == user.user_id:
            raise API_409_FRIEND_YOURSELF_EXCEPTION
        query = tables.friends.insert().values(
            user_id_1=friend_id if friend_id < user.user_id else user.user_id,
            user_id_2=friend_id if friend_id > user.user_id else user.user_id,
            action_user_id=user.user_id
        )
        try:
            await database.execute(query)
        except asyncpg.exceptions.UniqueViolationError:
            raise API_409_RELATIONSHIP_CONFLICT_EXCEPTION
        return {"detail": "friend relationship created"}
    else:
        raise API_404_USER_NOT_FOUND_EXCEPTION


async def update_friend_relationship(friend: Friend, user: User):
    friend_1 = friend.friend_id if friend.friend_id < user.user_id else user.user_id
    friend_2 = friend.friend_id if friend.friend_id > user.user_id else user.user_id
    query = select([tables.friends])\
        .where(tables.friends.c.user_id_1 == friend_1).where(tables.friends.c.user_id_2 == friend_2)
    relationship = dict(await database.fetch_one(query))
    if relationship['action_user_id'] == user.user_id and \
            relationship['relationship'] == models.friend_relationship.pending:
        raise API_401_FRIEND_REQUEST_EXCEPTION
    else:
        query = tables.friends.update()\
            .where(tables.friends.c.user_id_1 == friend_1).where(tables.friends.c.user_id_2 == friend_2) \
            .values(relationship=friend.relationship, action_user_id=user.user_id)
        await database.execute(query)
        return {"detail": "friend relationship updated"}


async def check_friend_relationship(friend_id: uuid.UUID, user_id: uuid.UUID):
    friend_1 = friend_id if friend_id < user_id else user_id
    friend_2 = friend_id if friend_id > user_id else user_id
    query = select([tables.friends]).where(tables.friends.c.user_id_1 == friend_1) \
        .where(tables.friends.c.user_id_2 == friend_2)
    relationship = await database.fetch_one(query)
    if relationship['relationship'] == models.friend_relationship.friends:
        return True
    else:
        raise API_404_RELATIONSHIP_EXCEPTION


# Events ---------------------------------------------------


async def create_event(event: Event, user: User):
    query = tables.events.insert().values(name=event.name, creator=user.user_id, venue=event.venue,
                                          visibility=event.visibility, time=event.time.replace(tzinfo=None))
    event.event_id = await database.execute(query)
    query = tables.users_events.insert().values(event_id=event.event_id, user_id=user.user_id, relationship='admin')
    await database.execute(query)
    return {**event.dict(), "creator": user.user_id}


async def get_public_events():
    query = select([tables.users_events.join(tables.events)])\
        .where(tables.events.c.visibility == event_visibility.public)
    result = await database.fetch_all(query)
    return result


async def get_friends_events(user: User):
    query = select([tables.events.join(tables.friends, tables.events.c.creator == tables.friends.c.user_id_1)])\
        .where(or_(tables.friends.c.user_id_1 == user.user_id, tables.friends.c.user_id_2 == user.user_id)) \
        .where(tables.users.c.user_id != user.user_id)\
        .where(tables.events.c.visibility != event_visibility.private)\
        .union(
        select([tables.events.join(tables.friends, tables.events.c.creator == tables.friends.c.user_id_2)])
        .where(or_(tables.friends.c.user_id_1 == user.user_id, tables.friends.c.user_id_2 == user.user_id))
        .where(tables.users.c.user_id != user.user_id)
        .where(tables.events.c.visibility != event_visibility.private))
    return await database.fetch_all(query)


async def get_private_events(user: User):
    query = select([tables.users_events.join(tables.events)])\
        .where(tables.users_events.c.user_id == user.user_id)\
        .where(tables.events.c.visibility == event_visibility.private)
    return await database.fetch_all(query)


















