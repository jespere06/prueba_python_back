import logging
from functools import wraps
from fastapi import HTTPException
from httpx import HTTPStatusError, RequestError, TimeoutException

logger = logging.getLogger(__name__)

def handle_api_error(func):
    
    @wraps(func)
    async def wrapper(*args, **kwargs):
        
        resource_id = f'para el ID {kwargs.get('id')}'
        
        try:
            return await func(*args, **kwargs)
            
        except TimeoutException as e:
            logger.error(f'Timeout al intentar conectar con la base de datos externa {resource_id}. URL:{e.request.url}')
            raise HTTPException(status_code=504, detail='La base de datos externa tardo demasiado en responder')
        
        except HTTPStatusError as e:
            if e.response.status_code == 404:
                logger.warning(f'Dato no encontrado (404) en la base de datos externa {resource_id}. URL={e.request.url}')      
                raise HTTPException(status_code=404, detail=f'El dato {resource_id} no fue encontrado')
            else:
                logger.error(f'Error HTTP ({e.response.status_code}) en la base de datos externa {resource_id}. URL={e.request.url}')      
                raise HTTPException(status_code=502, detail=f'Se recibio un dato invalido de la base de datos externa')
            
        except RequestError as e:
            logger.error(f'Error de conexion (503) con la base de datos externa {resource_id}. URL={e.request.url}')      
            raise HTTPException(status_code=503, detail=f'No se pudo establecer una conexion con la base de datos externa')
        
        except Exception as e:
            logger.exception(f'Error interno inesperado en el endpoint: "{func.__name}" {resource_id}: {e}')
            raise HTTPException(status_code=500, detail=f'Ocurrio un error interno en el servidor')

    return wrapper