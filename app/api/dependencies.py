from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session

from app import crud, models
from app.core.security import verify_token
from app.db.session import SessionLocal

basic_oauth = HTTPBasic()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db),
                     credentials: HTTPBasicCredentials = Depends(basic_oauth)) -> models.User:
    user = crud.user.get_by_username(db, username=credentials.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    is_valid_token = verify_token(credentials.password, user.hashed_password)
    if not is_valid_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user
