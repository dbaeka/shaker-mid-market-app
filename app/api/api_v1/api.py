from app.api.api_v1.endpoints import users, rates
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(rates.router, prefix="/rates", tags=["rates"])
