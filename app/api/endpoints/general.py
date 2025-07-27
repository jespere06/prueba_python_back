from fastapi import APIRouter, Request

from app.schemas.response import HealthCheck, HealthCheckResponse, Root, RootResponse
from app.utils.api_error_handler import handle_api_error

router = APIRouter()

@router.get('/', response_model = RootResponse)
@handle_api_error
async def read_root(request: Request):
    """
    Maneja el endpoint raiz '/' de la API.

    Recupera y devuelve información básica sobre la API, incluyendo 
    un mensaje de bienvenida, el nombre, descripción y versión de la API.

    Args:
        request (Request): El objeto de solicitud HTTP.

    Returns:
        RootResponse: Un objeto de respuesta que contiene la información 
                      raiz de la API.
    """

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
    """
    Maneja el endpoint de verificación de estado '/health' de la API.

    Realiza una verificación rápida del estado de la API y devuelve un 
    estado 'ok' simple en la respuesta si la API está funcionando 
    correctamente.

    Returns:
        HealthCheckResponse: Un objeto de respuesta que contiene el estado 
                             de verificaci n de la API.
    """
    return HealthCheckResponse(body=HealthCheck(status='ok'))
