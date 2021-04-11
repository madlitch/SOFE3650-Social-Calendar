from fastapi import FastAPI, Depends, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from database import database
from models import *
from typing import List

import time
import auth
import methods
import exceptions
import uuid

# uvicorn server:app --reload


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Endpoints ---------------------------------------------------


@app.get("/v1/teapot/")
async def teapot():
    raise exceptions.API_418_TEAPOT_EXCEPTION


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await auth.login(form_data)
    return token


@app.post("/v1/users/create", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn):
    return await methods.create_user(user)


@app.get("/v1/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
    return current_user


@app.get("/v1/friends/", response_model=List[FriendOut])
async def get_friends(current_user: User = Depends(auth.get_current_active_user)):
    return await methods.get_friends(current_user)


@app.post("/v1/friends/create/", status_code=status.HTTP_201_CREATED)
async def create_friend_relationship(friend: NewFriend, user: User = Depends(auth.get_current_active_user)):
    return await methods.create_friend_relationship(friend, user)


@app.post("/v1/friends/update/")
async def update_friend_relationship(friend: Friend, user: User = Depends(auth.get_current_active_user)):
    return await methods.update_friend_relationship(friend, user)


@app.get("/v1/events/", response_model=List[EventOut])
async def get_events(user: User = Depends(auth.get_current_active_user)):
    return await methods.get_events(user)


@app.get("/v1/events/friends")
async def get_public_events(user: User = Depends(auth.get_current_active_user)):
    return await methods.get_friends_events(user)


@app.post("/v1/events/create/", status_code=status.HTTP_201_CREATED, response_model=Event)
async def create_event(event: Event, user: User = Depends(auth.get_current_active_user)):
    return await methods.create_event(event, user)


@app.post("/v1/events/join")
async def join_event(event_id: uuid.UUID, user: User = Depends(auth.get_current_active_user)):
    return await methods.join_event(event_id, user)


@app.post("/v1/events/update/users")
async def update_event_users(event_users: EventUsersIn,  user: User = Depends(auth.get_current_active_user)):
    return await methods.update_event_users(event_users, user)


@app.post("/v1/events/update/relationship")
async def update_event_relationship(user: User = Depends(auth.get_current_active_user)):
    return await methods.update_event_relationship(user)



