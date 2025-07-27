from fastapi import FastAPI

from app.core.config import settings
from app.api.api import api_router
from .utils.logger_config import setup_logger

setup_logger()

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(api_router)