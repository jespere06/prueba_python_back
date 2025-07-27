from fastapi import APIRouter, Depends

from app.schemas.album import Album
from app.schemas.post import Post
from app.schemas.response import AlbumsResponse, PostsResponse, TodosResponse, UserResponse
from app.schemas.todos import Todos
from app.schemas.user import User
from app.services.external_api_service import ExternalApiService, get_api_service
from app.utils.api_error_handler import handle_api_error

router = APIRouter()


@router.get('/users/{id}', response_model = UserResponse)
@handle_api_error
async def get_user_info(id: int, service: ExternalApiService = Depends(get_api_service)):
    user_data = await service.get_user(id)

    user_info = User(**user_data)
    
    return UserResponse(body=user_info)


@router.get('/posts', response_model = PostsResponse)
@handle_api_error
async def get_user_posts(id: int, service: ExternalApiService = Depends(get_api_service)):
    posts_data = await service.get_user_posts(id)
    
    # Creacion de lista de Posts del Usuario
    posts = [Post(**post) for post in posts_data]
        
    return PostsResponse(body = posts)

@router.get('/albums', response_model = AlbumsResponse)
@handle_api_error
async def get_user_albums(id: int, service: ExternalApiService = Depends(get_api_service)):
    albums_data = await service.get_user_albums(id)
    
    # Creacion de lista de Posts del Usuario
    albums = [Album(**album) for album in albums_data]
        
    return AlbumsResponse(body = albums)

@router.get('/todos', response_model = TodosResponse)
@handle_api_error
async def get_user_todos(id: int, service: ExternalApiService = Depends(get_api_service)):
    todos_data = await service.get_user_todos(id)
    
    # Creacion de lista de Posts del Usuario
    todos = [Todos(**todos) for todos in todos_data]
        
    return TodosResponse(body = todos)
