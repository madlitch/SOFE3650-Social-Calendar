from pydantic import BaseModel
from typing import Optional
import enum
import datetime
import uuid

# Auth ---------------------------------------------------


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# User ---------------------------------------------------

class User(BaseModel):
    user_id: uuid.UUID = None
    username: str
    first_name: str
    last_name: str


class UserIn(User):
    password: str


class UserAuthIn(User):
    username: str
    hashed_password: str
    salt: str


class UserOut(BaseModel):
    user_id: uuid.UUID
    username: str
    first_name: str
    last_name: str


# Friends ---------------------------------------------------

class friend_relationship(enum.Enum):
    pending = "pending"
    friends = "friends"
    declined = "declined"


class Friend(BaseModel):
    friend_id: uuid.UUID
    relationship: friend_relationship = "pending"


class NewFriend(BaseModel):
    username: str
    relationship: friend_relationship = "pending"


class FriendOut(BaseModel):
    user_id: uuid.UUID
    username: str
    first_name: str
    last_name: str
    relationship: friend_relationship


# Event ---------------------------------------------------


class event_visibility(enum.Enum):
    private = "private"
    friends = "friends"
    public = "public"


class Event(BaseModel):
    event_id: uuid.UUID = None
    name: str
    creator: uuid.UUID = None
    visibility: event_visibility = "private"
    venue: Optional[str] = None
    time: datetime.datetime


class EventOut(BaseModel):
    event_id: uuid.UUID = None
    name: str
    creator: uuid.UUID = None
    visibility: event_visibility = "private"
    venue: Optional[str] = None
    time: datetime.datetime
