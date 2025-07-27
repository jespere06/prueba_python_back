import httpx

BASE_URL = 'https://jsonplaceholder.typicode.com'

DEFAULT_TIMEOUT = httpx.Timeout(10, connect=5)

class FetchEngine:   
    
    # Funcion de peticion maestra y centralizada
    async def _fetch(self, endpoint: str):
        url = f'{BASE_URL}/{endpoint}'
        
        try:
            async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
                response = await client.get(url)
                
                # [ Verificacion de error ]
                response.raise_for_status()
                    
                return response.json()

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            raise
            
    
    async def get_user(self, user_id):   
        return await self._fetch(f'users/{user_id}')
    
    async def get_user_albums(self, user_id):
        await self.get_user(user_id)
        return await self._fetch(f'users/{user_id}/albums')
    
    async def get_user_todos(self, user_id):
        await self.get_user(user_id)
        return await self._fetch(f'users/{user_id}/todos')

    async def get_user_posts(self, user_id):
        await self.get_user(user_id)
        return await self._fetch(f'users/{user_id}/posts')
