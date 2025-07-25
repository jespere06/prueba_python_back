import asyncio
from fastapi import FastAPI
from fetch_engine import FetchEngine
from models import FetchEngineResponse, Post, User

app = FastAPI()
fetcher = FetchEngine()

@app.get('/users/{id}', response_model=FetchEngineResponse)
async def fetch_user_info(id: int):

    # Creacion de Tasks a consultar
    albums_task = fetcher.user_albums(id)
    todos_task = fetcher.user_todos(id)
    posts_task = fetcher.user_posts(id)
    
    # Aprovechamiento de httpx para evitar que sea secuencial
    user_albums, user_todos, user_posts = await asyncio.gather(albums_task, todos_task, posts_task)
    
    user_info = User(user_id=id, albums=user_albums, todos=user_todos, posts=user_posts)
    
    return FetchEngineResponse(body=user_info)
    


@app.get('/posts', response_model=FetchEngineResponse)
async def fetch_user_posts(id: int):
    
    posts_data = await fetcher.user_posts(id)
    
    # Creacion de lista de Posts del Usuario
    posts = [Post(**post) for post in posts_data]
        
    return FetchEngineResponse(body=posts)

