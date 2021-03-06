from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database import database
from models import *
from typing import List

import auth
import methods
import exceptions

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


@app.post("/v1/users/create", response_model=User)
async def create_user(user: UserIn):
    return await methods.create_user(user)


@app.get("/v1/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
    return current_user


@app.get("/v1/friends/", response_model=List[FriendOut])
async def get_friends(current_user: User = Depends(auth.get_current_active_user)):
    return await methods.get_friends(current_user)


@app.post("/v1/friends/create/")
async def create_friend_relationship(friend: NewFriend, user: User = Depends(auth.get_current_active_user)):
    return await methods.create_friend_relationship(friend, user)


@app.post("/v1/events/create/",  response_model=Event)
async def create_event(event: Event, user: User = Depends(auth.get_current_active_user)):
    return await methods.create_event(event, user)


@app.get("/v1/events/public", response_model=List[EventOut])
async def get_public_events(user: User = Depends(auth.get_current_active_user)):
    return await methods.get_public_events()


@app.get("/v1/events/friends", response_model=List[EventOut])
async def get_friends_events(user: User = Depends(auth.get_current_active_user)):
    return await methods.get_friends_events(user)


@app.get("/v1/events/private", response_model=List[EventOut])
async def get_private_events(user: User = Depends(auth.get_current_active_user)):
    return await methods.get_private_events(user)






