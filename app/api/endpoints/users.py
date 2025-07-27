from typing import Any
from fastapi import APIRouter, Depends

from app.schemas.album import Album
from app.schemas.post import Post
from app.schemas.response import AlbumsResponse, ErrorDetail, PostsResponse, TodosResponse, UserResponse
from app.schemas.todos import Todos
from app.schemas.user import User
from app.services.external_api_service import ExternalApiService, get_api_service
from app.utils.api_error_handler import handle_api_error
from typing import Any

router = APIRouter()


RESPONSES: dict[int | str, dict[str, Any]] = {
    404: {"model": ErrorDetail, "description": "El usuario no ha sido encontrado."},
    502: {"model": ErrorDetail, "description": "Se recibió una respuesta inválida del servicio externo."},
    503: {"model": ErrorDetail, "description": "No se pudo establecer conexión con el servicio externo."},
    504: {"model": ErrorDetail, "description": "El servicio externo tardó demasiado en responder."}
}

@router.get('/users/{id}', response_model = UserResponse, responses=RESPONSES)
@handle_api_error
async def get_user_info(id: int, service: ExternalApiService = Depends(get_api_service)):
    """
    Retorna la información del usuario para el id proporcionado.

    Args:
        id (int): El id del usuario del cual se va a recuperar la información.

    Returns:
        UserResponse: La respuesta que contiene la información del usuario o un mensaje de error.
    """
    user_data = await service.get_user(id)

    user_info = User(**user_data)
    
    return UserResponse(body=user_info)


@router.get('/posts', response_model = PostsResponse, responses=RESPONSES)
@handle_api_error
async def get_user_posts(id: int, service: ExternalApiService = Depends(get_api_service)):
    """
    Retorna una lista de posts de un usuario.

    Args:
        id (int): El id del usuario del que se van a obtener los posts.

    Returns:
        PostsResponse: La respuesta que contiene la lista de posts o un mensaje de error.
    """
    posts_data = await service.get_user_posts(id)
    
    # Creacion de lista de Posts del Usuario
    posts = [Post(**post) for post in posts_data]
        
    return PostsResponse(body = posts)

@router.get('/albums', response_model = AlbumsResponse, responses=RESPONSES)
@handle_api_error
async def get_user_albums(id: int, service: ExternalApiService = Depends(get_api_service)):
    """
    Retorna una lista de álbumes para un usuario especificado.

    Args:
        id (int): El id del usuario del que se van a obtener los álbumes.

    Returns:
        AlbumsResponse: La respuesta que contiene la lista de álbumes o un mensaje de error.
    """

    albums_data = await service.get_user_albums(id)
    
    # Creacion de lista de Posts del Usuario
    albums = [Album(**album) for album in albums_data]
        
    return AlbumsResponse(body = albums)

@router.get('/todos', response_model = TodosResponse, responses=RESPONSES)
@handle_api_error
async def get_user_todos(id: int, service: ExternalApiService = Depends(get_api_service)):
    """
    Retorna una lista de tareas de un usuario.

    Args:
        id (int): El id del usuario del que se van a obtener las tareas.

    Returns:
        TodosResponse: La respuesta que contiene la lista de tareas o un mensaje de error.
    """
    todos_data = await service.get_user_todos(id)
    
    # Creacion de lista de Posts del Usuario
    todos = [Todos(**todos) for todos in todos_data]
        
    return TodosResponse(body = todos)
