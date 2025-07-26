import asyncio
import logging
from fastapi import FastAPI, HTTPException
from httpx import HTTPStatusError, RequestError

from fetch_engine import FetchEngine
from models import Post, User, UserAllData, UserResponse, UserAllDataResponse, PostsResponse
from logger import setup_logger

# [ Configuraccion ]
setup_logger()
logger = logging.getLogger(__name__)
app = FastAPI()
fetcher = FetchEngine()

# [ Endpoints ]
# TODO: Crear un wrapper centralizado para el manejo de errores de forma optima
# PSD: la API no devuelve errores en lugar esta vacia la respuesta, corregir esto ya que fallara la logica

@app.get('/users/{id}', response_model=UserResponse)
async def get_user_info(id: int):
    try:
        user_data = await fetcher.get_user(id)

        user_info = User(**user_data)
        
        return UserResponse(body=user_info)
    except HTTPStatusError as e:
        if e.response.status_code == 404:
            logger.warning(f'Intento de acesso a usuario inexistente: {id}')
            raise HTTPException(status_code=404, detail=f'Usuario con el id ({id}) no encontrado')
        else:
            logger.warning(f'Error HTTP inesperado por: {id}')
            raise HTTPException(status_code=500, detail='Error en la base de datos')
    except RequestError as e:
        logger.error(f'Error de red obteniendo a usuario: {id}')
        raise HTTPException(status_code=503, detail='No se pudo conectar con la base de datos')   

@app.get('/posts', response_model=PostsResponse)
async def get_user_posts(id: int):
    try:
        posts_data = await fetcher.get_user_posts(id)
        
        # Creacion de lista de Posts del Usuario
        posts = [Post(**post) for post in posts_data]
            
        return PostsResponse(body=posts)
    
    except HTTPStatusError as e:
        if e.response.status_code == 404:
            logger.warning(f'Intento de acesso a usuario inexistente: {id}')
            raise HTTPException(status_code=404, detail=f'Usuario con el id ({id}) no encontrado')
        else:
            logger.warning(f'Error HTTP inesperado por: {id}')
            raise HTTPException(status_code=500, detail='Error en la base de datos')
    except RequestError as e:
        logger.error(f'Error de red obteniendo a usuario: {id}')
        raise HTTPException(status_code=503, detail='No se pudo conectar con la base de datos')

@app.get('/users/{id}/all-data', response_model=UserAllDataResponse)
async def get_all_user_data(id: int):
    try:
        # Creacion de Tasks a consultar
        albums_task = fetcher.get_user_albums(id)
        todos_task = fetcher.get_user_todos(id)
        posts_task = fetcher.get_user_posts(id)
        
        # Aprovechamiento de httpx para evitar que sea secuencial
        user_albums, user_todos, user_posts = await asyncio.gather(albums_task, todos_task, posts_task)
        
        user_data = UserAllData(user_id=id, albums=user_albums, todos=user_todos, posts=user_posts)
        
        return UserAllDataResponse(body=user_data)
    
    except HTTPStatusError as e:
        if e.response.status_code == 404:
            logger.warning(f'Intento de acesso a usuario inexistente: {id}')
            raise HTTPException(status_code=404, detail=f'Usuario con el id ({id}) no encontrado')
        else:
            logger.warning(f'Error HTTP inesperado por: {id}')
            raise HTTPException(status_code=500, detail='Error en la base de datos')
    except RequestError as e:
        logger.error(f'Error de red obteniendo a usuario: {id}')
        raise HTTPException(status_code=503, detail='No se pudo conectar con la base de datos')
       