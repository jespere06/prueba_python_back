
# [ Modelos de Respuesta ]
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_serializer

from app.schemas.album import Album
from app.schemas.post import Post
from app.schemas.todos import Todos
from app.schemas.user import User

class Root(BaseModel):
    message: str
    name: str
    description: str
    version: str
    model_config = ConfigDict(from_attributes=True)
    
class HealthCheck(BaseModel):
    status: str


class BaseResponse(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    
    @field_serializer('timestamp')
    def serialize_timestamp(self, timestamp: datetime):
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
class RootResponse(BaseResponse):
    body: Root = Field(default=...)

class HealthCheckResponse(BaseResponse):
    body: HealthCheck = Field(default=...)

class UserResponse(BaseResponse):
    body: User = Field(default=...)
        
class PostsResponse(BaseResponse):
    body: list[Post] = Field(default=...)
    
class AlbumsResponse(BaseResponse):
    body: list[Album] = Field(default=...)

class TodosResponse(BaseResponse):
    body: list[Todos] = Field(default=...)
    
    

    