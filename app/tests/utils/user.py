import base64
from typing import Dict

from sqlalchemy.orm import Session

from app import crud
from app.models.user import User
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_lower_string


def user_authentication_headers(*, username: str, password: str) -> Dict[str, str]:
    key = f"{username}:{password}"
    key_bytes = key.encode("utf8")
    token = base64.b64encode(key_bytes).decode("utf8")
    headers = {"Authorization": f"Basic {token}"}
    return headers


def create_random_user(db: Session) -> User:
    username = random_lower_string()
    password = random_lower_string()
    user_in = UserCreate(username=username, password=password)
    user = crud.user.create(db=db, obj_in=user_in)
    return user
