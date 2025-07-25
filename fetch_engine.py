import httpx
import logging

BASE_URL = 'https://jsonplaceholder.typicode.com'

logger = logging.getLogger(__name__)

class FetchEngine:   
    
    # Funcion de peticion maestra y centralizada
    async def _fetch(self, endpoint: str):
        url = f'{BASE_URL}/{endpoint}'
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                return response.json()
        except httpx.HTTPError as e:
            logger.error(f'Ha ocurrido un error: {e}')
            raise
    
    async def user_albums(self, user_id):   
        return await self._fetch(f'users/{user_id}/albums')
    
    async def user_todos(self, user_id):
        return await self._fetch(f'users/{user_id}/todos')

    async def user_posts(self, user_id):
        return await self._fetch(f'users/{user_id}/posts')