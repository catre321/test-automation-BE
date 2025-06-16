# filepath: fastapi-sqlmodel-backend/app/api/v1/endpoints/__init__.py
from fastapi import APIRouter

router = APIRouter()

from . import users

router.include_router(users.router, prefix="/users", tags=["users"])