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
    if len(user.username) < 3:
        raise API_406_USERNAME_EXCEPTION
    query = tables.users.select().where(tables.users.c.username == user.username)
    existing_user = await database.execute(query)
    if existing_user:
        raise API_409_USERNAME_CONFLICT_EXCEPTION
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


async def create_event(event: EventIn, user: User):
    query = tables.events.insert().values(name=event.name, creator=user.user_id, venue=event.venue,
                                          visibility=event.visibility)
    event.event_id = await database.execute(query)
    query = tables.users_events.insert().values(event_id=event.event_id, user_id=user.user_id, relationship='admin')
    await database.execute(query)
    await add_event_users(event.users, event.event_id, user)
    return {**event.dict(), "creator": user.user_id}


async def join_event(event_id: uuid.UUID, user: User):
    query = select([tables.events]).where(tables.events.c.event_id == event_id)
    event = await database.fetch_one(query)
    query = tables.users_events.insert().values(event_id=event_id, user_id=user.user_id, relationship='attending')
    if event['visibility'] == models.event_visibility.public:
        try:
            await database.execute(query)
        except asyncpg.UniqueViolationError:
            raise API_409_RELATIONSHIP_CONFLICT_EXCEPTION
    elif event['visibility'] == models.event_visibility.friends:
        if await check_friend_relationship(event['creator'], user.user_id):
            try:
                await database.execute(query)
            except asyncpg.UniqueViolationError:
                raise API_409_RELATIONSHIP_CONFLICT_EXCEPTION
    elif event['visibility'] == models.event_visibility.private:
        raise API_401_EVENT_ADMIN_EXCEPTION


async def update_event_users(event_in, user: User):
    query = select([tables.events]).where(tables.events.c.event_id == event_in.event_id)
    event = dict(await database.fetch_one(query))
    if event:
        if event['visibility'] == models.event_visibility.public:
            return await add_event_users(event_in.users, event_in.event_id, user)
        elif event['visibility'] == models.event_visibility.friends:
            if check_friend_relationship(event['creator'], user.user_id):
                return await add_event_users(event_in.users, event_in.event_id, user)
        elif event['visibility'] == models.event_visibility.private:
            if await check_user_event_admin_relationship(event_in.event_id, user.user_id):
                return await add_event_users(event_in.users, event_in.event_id, user)


async def add_event_users(users: list, event_id: uuid.UUID, user: User):
    if None not in users:
        for inv_users in users:
            await check_friend_relationship(inv_users.user_id, user.user_id)
    values = []
    for user_id in users:
        values.append({'event_id': event_id, 'user_id': user_id, 'relationship': 'invited'})
    query = tables.users_events.insert()
    try:
        await database.execute_many(query, values)
    except asyncpg.exceptions.ForeignKeyViolationError:
        raise API_404_USER_NOT_FOUND_EXCEPTION
    except asyncpg.exceptions.UniqueViolationError:
        raise API_409_RELATIONSHIP_CONFLICT_EXCEPTION
    return {"detail": "user(s) added"}


async def check_user_event_relationship(event_id: uuid.UUID, user_id: uuid.UUID):
    query = tables.users_events.select().where(tables.users_events.c.user_id == user_id)\
        .where(tables.users_events.c.event_id == event_id)
    existing_relationship = await database.execute(query)
    if existing_relationship:
        return True
    else:
        raise API_401_EVENT_CREDENTIALS_EXCEPTION


async def check_user_event_admin_relationship(event_id: uuid.UUID, user_id: uuid.UUID):
    query = select([tables.users_events.c.relationship]) \
        .where(tables.users_events.c.user_id == user_id) \
        .where(tables.users_events.c.event_id == event_id)
    is_admin = await database.fetch_one(query)
    if is_admin:
        if is_admin['relationship'] == models.users_event_relationship.admin:
            return True
        else:
            raise API_401_EVENT_ADMIN_EXCEPTION
    else:
        raise API_401_EVENT_ADMIN_EXCEPTION


async def update_event_name(event_name: EventUpdateName, user: User):
    if await check_user_event_admin_relationship(event_name.event_id, user.user_id):
        query = tables.events.update()\
            .where(tables.events.c.event_id == event_name.event_id)\
            .values(name=event_name.name)
        await database.execute(query)
        return {'detail': 'name changed successfully'}


async def update_event_relationship(event_data: EventUpdateRelationship, user: User):
    query = tables.users_events.update()\
        .where(tables.users_events.c.user_id == user.user_id)\
        .where(tables.users_events.c.event_id == event_data.event_id)\
        .values(tables.users_events.c.relationship == event_data.relationship)
    if await database.execute(query):
        return {'detail': 'relationship updated successfully'}
    else:
        raise API_404_RELATIONSHIP_EXCEPTION


async def get_events(user: User):
    query = select([tables.users_events.join(tables.events)])\
        .where(tables.users_events.c.user_id == user.user_id)
    result = await database.fetch_all(query)
    events = []
    for row in result:
        events.append(EventOut(event_id=row['event_id'],
                               members=await get_event_users(row['event_id']),
                               name=row['name'],
                               creator=row['creator'],
                               visibility=row['visibility'],
                               venue=row['venue'],
                               time=row['time']))
    return events


async def get_event_users(event_id: uuid.UUID, user: User = None):
    if not user or await check_user_event_relationship(event_id, user.user_id):
        query = select([tables.users_events.join(tables.users)]) \
            .where(tables.users_events.c.event_id == event_id)
        result = await database.fetch_all(query)
        users = []
        for row in result:
            users.append(UserOut(user_id=row['user_id'],
                                 username=row['username'],
                                 first_name=row['first_name'],
                                 last_name=row['last_name']))
        return users


async def get_event_user_ids(event_id: uuid.UUID, user: User = None):
    if not user or await check_user_event_relationship(event_id, user.user_id):
        query = select([tables.users_events.c.user_id])\
            .where(tables.users_events.c.event_id == event_id)
        result = [row['user_id'] for row in await database.fetch_all(query)]
        return result


async def get_friends_events(user: User):
    print(get_friends(user))
    query = select([tables.events])\
        .where(tables.events.c.visibility == event_visibility.friends)
    result = await database.fetch_all(query)
    return result

















