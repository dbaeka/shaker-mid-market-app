from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base
from app.db.session import engine


def init_db(db: Session) -> None:
    base.Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_username(db, settings.TEST_USER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.TEST_USER,
            password=settings.TEST_USER_PASSWORD
        )
        user = crud.user.create(db, obj_in=user_in)
