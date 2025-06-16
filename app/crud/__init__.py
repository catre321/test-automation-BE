# filepath: fastapi-sqlmodel-backend/app/crud/__init__.py
from .base import CRUDBase
from .user_crud import user_crud

__all__ = ["CRUDBase", "user_crud"]