from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = 'JSONPlaceholder API'
    JSONPLACEHOLDER_BASE_URL: str | None = None
    
    class config:
        env_file = '.env'
        
        
settings = Settings()