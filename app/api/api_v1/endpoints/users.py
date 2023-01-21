from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, models
from app.api.dependencies import get_db, get_current_user
from app.core.config import logger

router = APIRouter()


@router.get("/me", response_model=schemas.User)
def read_user_me(
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user),
) -> Any:
    """
    Get current user.
    """
    logger.info("Getting Current User: " + current_user.username)
    return current_user
