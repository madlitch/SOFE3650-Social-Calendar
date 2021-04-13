from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from models import UserAuthIn, User, TokenData
from tables import users
from database import database

import bcrypt
import exceptions
import constants


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 300


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, salt, hashed_password):
    return pwd_context.verify(plain_password + salt, hashed_password)


def get_password_hash(password_and_salt):
    return pwd_context.hash(password_and_salt)


def gen_salt():
    return str(bcrypt.gensalt(10))


async def get_user(username: str):
    query = users.select().where(users.c.username == username.lower())
    user = await database.fetch_one(query)
    if user:
        return UserAuthIn(**user)


async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not verify_password(password, user.salt, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, constants.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, constants.SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise exceptions.API_401_CREDENTIALS_EXCEPTION
        token_data = TokenData(username=username)
    except JWTError:
        raise exceptions.API_401_CREDENTIALS_EXCEPTION
    user = await get_user(username=token_data.username)
    if user is None:
        raise exceptions.API_401_CREDENTIALS_EXCEPTION
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


async def login(form_data):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

