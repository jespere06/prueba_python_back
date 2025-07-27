# [ Endpoints ]
from fastapi import APIRouter, Request

from app.schemas.response import HealthCheck, HealthCheckResponse, Root, RootResponse
from app.utils.api_error_handler import handle_api_error

router = APIRouter()

@router.get('/', response_model = RootResponse)
@handle_api_error
async def read_root(request: Request):
    app_instance = request.app
    root_data = {
        'message': 'Bienvenido a la API de base de datos de JSONPlaceholder.',
        'name': app_instance.title,
        'description': app_instance.description,
        'version': app_instance.version
    }
    return RootResponse(body=Root(**root_data))

@router.get('/health', response_model = HealthCheckResponse)
@handle_api_error
async def check_status():
    return HealthCheckResponse(body=HealthCheck(status='ok'))
