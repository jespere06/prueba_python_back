from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = 'JSONPlaceholder API'
    JSONPLACEHOLDER_BASE_URL: str | None = 'https://jsonplaceholder.typicode.com'
    VERSION: str = '1.0.0'
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
        
        
settings = Settings()