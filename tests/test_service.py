import pytest
import respx
from httpx import Response

from app.services.external_api_service import ExternalApiService
from .data import MOCK_USER_DATA, MOCK_TODOS_DATA, MOCK_POSTS_DATA, MOCK_ALBUMS_DATA

pytestmark = pytest.mark.asyncio
BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_service():
    """
    Un fixture que devuelve una instancia de ExternalApiService, lista para usar.

    El fixture es un objeto que se utiliza en un test, que se encarga de
    inicializar y configurar el objeto o los objetos que se van a probar.
    En este caso, el fixture api_service devuelve una instancia de
    ExternalApiService, lista para ser utilizada en los tests.
    """
    return ExternalApiService()

@respx.mock
async def test_get_user(api_service: ExternalApiService):
    """
    Prueba que el metodo get_user de ExternalApiService devuelve la informacion
    del usuario solicitado.

    La prueba utiliza el mock de respx para interceptar la peticion a la API
    externa y devuelve la respuesta mockeada con la informacion del usuario
    solicitado. Luego se verifica que el objeto devuelto por get_user sea
    igual al esperado.
    """
    respx.get(f"{BASE_URL}/users/1").mock(return_value=Response(200, json=MOCK_USER_DATA))
    user = await api_service.get_user(1)
    assert user == MOCK_USER_DATA
    
@respx.mock
async def test_get_user_posts(api_service: ExternalApiService):  
    """
    Prueba que el metodo get_user_posts de ExternalApiService devuelve la lista de posts
    del usuario solicitado.

    La prueba utiliza el mock de respx para interceptar la peticion a la API
    externa y devuelve la respuesta mockeada con la lista de posts del usuario
    solicitado. Luego se verifica que el objeto devuelto por get_user_posts sea
    igual al esperado.
    """
    
    respx.get(f"{BASE_URL}/users/1").mock(return_value=Response(200, json=MOCK_USER_DATA))
    
    respx.get(f"{BASE_URL}/users/1/posts").mock(return_value=Response(200, json=MOCK_POSTS_DATA))
    posts = await api_service.get_user_posts(1)
    assert posts == MOCK_POSTS_DATA
    
@respx.mock
async def test_get_user_todos(api_service: ExternalApiService):  
    """
    Prueba que el metodo get_user_todos de ExternalApiService devuelve la lista de tareas
    del usuario solicitado.

    La prueba utiliza el mock de respx para interceptar la peticion a la API
    externa y devuelve la respuesta mockeada con la lista de tareas del usuario
    solicitado. Luego se verifica que el objeto devuelto por get_user_todos sea
    igual al esperado.
    """
    
    respx.get(f"{BASE_URL}/users/1").mock(return_value=Response(200, json=MOCK_USER_DATA))
    
    respx.get(f"{BASE_URL}/users/1/todos").mock(return_value=Response(200, json=MOCK_TODOS_DATA))
    todos = await api_service.get_user_todos(1)
    assert todos == MOCK_TODOS_DATA

@respx.mock
async def test_get_user_albums(api_service: ExternalApiService):  
    """
    Prueba que el metodo get_user_albums de ExternalApiService devuelve la lista de álbumes
    del usuario solicitado.

    La prueba utiliza el mock de respx para interceptar la peticion a la API
    externa y devuelve la respuesta mockeada con la lista de álbumes del usuario
    solicitado. Luego se verifica que el objeto devuelto por get_user_albums sea
    igual al esperado.
    """
    
    respx.get(f"{BASE_URL}/users/1").mock(return_value=Response(200, json=MOCK_USER_DATA))
    
    respx.get(f"{BASE_URL}/users/1/albums").mock(return_value=Response(200, json=MOCK_ALBUMS_DATA))
    albums = await api_service.get_user_albums(1)
    assert albums == MOCK_ALBUMS_DATA
    