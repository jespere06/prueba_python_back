import httpx
from app.core.config import settings 

BASE_URL = settings.JSONPLACEHOLDER_BASE_URL

DEFAULT_TIMEOUT = httpx.Timeout(10, connect=5)

class ExternalApiService:   
    async def _fetch(self, endpoint: str):
        """
        Función centralizada para obtener datos de la API.

        Argumentos:
            endpoint (str): El endpoint desde el cual obtener los datos.

        Retorna:
            dict: La respuesta que contiene los datos obtenidos de la API.
        """
        url = f'{BASE_URL}/{endpoint}'      

        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            response = await client.get(url)
            
            # [ Verificacion de error ]
            response.raise_for_status()
                
            return response.json()     
    
    async def get_user(self, user_id):   
        """
        Obtiene información del usuario desde la API.

        Argumentos:
            user_id (int): El id del usuario a obtener la informaci n.

        Retorna:
            dict: La respuesta que contiene la información del usuario.
        """
        return await self._fetch(f'users/{user_id}')
    
    async def get_user_albums(self, user_id):
        """
        Recupera la lista de albums para un usuario determinado.

        Argumentos:
            user_id (int): El id del usuario para obtener la lista de albums.

        Retorna:
            list: La respuesta que contiene la lista de albums.

        Lanza:
            HTTPException: Si el usuario no ha sido encontrado.
        """
        await self.get_user(user_id)
        return await self._fetch(f'users/{user_id}/albums')
    
    async def get_user_todos(self, user_id):
        """
        Recupera la lista de tareas pendientes para un usuario determinado.

        Argumentos:
            user_id (int): El id del usuario para obtener la lista de tareas pendientes.

        Retorna:
            list: La respuesta que contiene la lista de tareas pendientes.

        Lanza:
            HTTPException: Si el usuario no ha sido encontrado.
        """
        
        await self.get_user(user_id)
        return await self._fetch(f'users/{user_id}/todos')

    async def get_user_posts(self, user_id):
        """
        Recupera la lista de publicaciones para un usuario determinado.

        Argumentos:
            user_id (int): El id del usuario para obtener la lista de publicaciones.

        Retorna:
            list: La respuesta que contiene la lista de publicaciones.

        Lanza:
            HTTPException: Si el usuario no ha sido encontrado.
        """
        
        await self.get_user(user_id)
        return await self._fetch(f'users/{user_id}/posts')

external_api_service = ExternalApiService()

def get_api_service():
    """
    Retorna una instancia de ExternalApiService.

    Esta función se utiliza para proporcionar una instancia de la clase ExternalApiService al sistema de
    inyección de dependencias de FastAPI.

    Retorna:
        ExternalApiService: La instancia de ExternalApiService.
    """
    return external_api_service
