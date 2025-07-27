from fastapi import APIRouter
from .endpoints import general, users

api_router = APIRouter()

api_router.include_router(general.router)
api_router.include_router(users.router)