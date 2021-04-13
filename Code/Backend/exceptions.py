from fastapi import HTTPException, status


API_401_CREDENTIALS_EXCEPTION = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


API_409_RELATIONSHIP_CONFLICT_EXCEPTION = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="relationship already exists"
        )

API_409_FRIEND_YOURSELF_EXCEPTION = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="you can't be friends with yourself"
        )

API_404_USER_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="user does not exist"
)

API_409_USERNAME_CONFLICT_EXCEPTION = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username already exists"
        )

API_406_USERNAME_EXCEPTION = HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="username does not follow guidelines"
        )

API_406_PASSWORD_EXCEPTION = HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="password does not follow guidelines"
        )

API_418_TEAPOT_EXCEPTION = HTTPException(
    status_code=418,
    detail="I'm a teapot",
)
