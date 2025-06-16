from fastapi import APIRouter
from app.api.v1.endpoints import users, projects

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])