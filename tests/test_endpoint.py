import pytest
from unittest.mock import MagicMock, AsyncMock
from fastapi.testclient import TestClient
from .data import MOCK_USER_DATA, MOCK_ALBUMS_DATA, MOCK_POSTS_DATA, MOCK_TODOS_DATA

from app.main import app
from app.services.external_api_service import get_api_service

pytestmark = pytest.mark.asyncio

mock_service = MagicMock()

def override_get_api_service():
    """
    Sobreescribe la función get_api_service para devolver una instancia de prueba.

    Returns:
        ExternalApiService: Una instancia de prueba de ExternalApiService.
    """
    return mock_service

app.dependency_overrides[get_api_service] = override_get_api_service

client = TestClient(app)


async def test_read_root():
    """
    Prueba que el endpoint raiz '/' devuelva un estatus 200.
    """
    response = client.get("/")
    assert response.status_code == 200
    
async def test_check_status():
    """
    Prueba que el endpoint de verificación de estado '/health' devuelva un estatus 200.
    """
    response = client.get("/health")
    assert response.status_code == 200
    
async def test_get_user():
    """
    Prueba que el endpoint de obtención de usuario '/users/{user_id}' devuelva un estatus 200.
    """
    mock_service.get_user = AsyncMock(return_value=MOCK_USER_DATA)
    response = client.get("/users/1")
    assert response.status_code == 200
    
async def test_get_user_posts(id: int = 1):
    """
    Prueba que el endpoint de obtención de posts 'posts/{user_id}' devuelva un estatus 200.
    """
    
    mock_service.get_user_posts = AsyncMock(return_value=MOCK_POSTS_DATA)
    
    response = client.get("/posts", params={"id": id})
    assert response.status_code == 200
    
async def test_get_user_todos(id: int = 1):
    """
    Prueba que el endpoint de obtención de tareas 'todos/{user_id}' devuelva un estatus 200.
    """
    
    mock_service.get_user_todos = AsyncMock(return_value=MOCK_TODOS_DATA)
    
    response = client.get("/todos", params={"id": id})
    assert response.status_code == 200

async def test_get_user_albums(id: int = 1):
    """
    Prueba que el endpoint de obtención de albums 'albums/{user_id}' devuelva un estatus 200.
    """
    
    mock_service.get_user_albums = AsyncMock(return_value=MOCK_ALBUMS_DATA)
    
    response = client.get("/albums", params={"id": id})
    assert response.status_code == 200
