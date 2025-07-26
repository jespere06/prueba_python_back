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
                
                # [ Verificacion de error ]
                response.raise_for_status()
                    
                return response.json()

        except httpx.RequestError as e:
            logger.error(f'Error de Conexion al intentar consultar {url}')
            raise
            
    
    async def get_user(self, user_id):   
        return await self._fetch(f'users/{user_id}')
    
    async def get_user_albums(self, user_id):   
        return await self._fetch(f'users/{user_id}/albums')
    
    async def get_user_todos(self, user_id):
        return await self._fetch(f'users/{user_id}/todos')

    async def get_user_posts(self, user_id):
        return await self._fetch(f'users/{user_id}/posts')
