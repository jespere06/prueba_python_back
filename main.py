from fastapi import FastAPI
from fetch_engine import FetchEngine
from models import FetchEngineResponse, Post, User

app = FastAPI()
fetcher = FetchEngine()

@app.get('/users/{id}', response_model=FetchEngineResponse)
async def fetch_user_info(id: int):
    return FetchEngineResponse(body=User(user_id=id, albums=await fetcher.user_albums(id), todos=await fetcher.user_todos(id), posts=await fetcher.user_posts(id)))

@app.get('/posts', response_model=FetchEngineResponse)
async def fetch_posts(id: int):
    
    posts = []
    
    for post in await fetcher.user_posts(id):
        posts.append(Post(**post))
        
    return FetchEngineResponse(body=posts)