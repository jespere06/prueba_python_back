import logging
from fastapi import FastAPI

from fetch_engine import FetchEngine
from models import User, UserResponse, Post, PostsResponse, Album, AlbumsResponse, Todos, TodosResponse
from logger import setup_logger
from api_error_handler import handle_api_error

# [ Configuraccion ]
setup_logger()
logger = logging.getLogger(__name__)
app = FastAPI()
fetcher = FetchEngine()

# [ Endpoints ]

@app.get('/users/{id}', response_model=UserResponse)
@handle_api_error
async def get_user_info(id: int):
    user_data = await fetcher.get_user(id)

    user_info = User(**user_data)
    
    return UserResponse(body=user_info)


@app.get('/posts', response_model=PostsResponse)
@handle_api_error
async def get_user_posts(id: int):
    posts_data = await fetcher.get_user_posts(id)
    
    # Creacion de lista de Posts del Usuario
    posts = [Post(**post) for post in posts_data]
        
    return PostsResponse(body=posts)

@app.get('/albums', response_model=AlbumsResponse)
@handle_api_error
async def get_user_albums(id: int):
    albums_data = await fetcher.get_user_albums(id)
    
    # Creacion de lista de Posts del Usuario
    albums = [Album(**album) for album in albums_data]
        
    return AlbumsResponse(body=albums)

@app.get('/todos', response_model=TodosResponse)
@handle_api_error
async def get_user_todos(id: int):
    todos_data = await fetcher.get_user_todos(id)
    
    # Creacion de lista de Posts del Usuario
    todos = [Todos(**todos) for todos in todos_data]
        
    return TodosResponse(body=todos)
