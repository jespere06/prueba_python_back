from pydantic import BaseModel, ConfigDict, Field, field_serializer, EmailStr
from datetime import datetime

# [ Modelos Generales ]
class Post(BaseModel):
    user_id: int = Field(alias='userId')
    post_id: int = Field(alias='id')
    title: str
    body: str
    model_config = ConfigDict(populate_by_name=True)
# TODO: seguir con Albums y Todos


# [ Modelos de User ]
class Geo(BaseModel):
    lat: str
    lng: str

class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo
    
class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str
    
class User(BaseModel):
    user_id: int = Field(alias='id')
    username: str
    email: EmailStr
    address: Address
    phone: str
    website: str # añadir un Field y un FieldValidator para añadir el https://
    company: Company
    model_config = ConfigDict(populate_by_name=True)
    
class UserAllData(BaseModel):
    user_id: int
    albums: list[dict] # TODO: Remplazar dict por Modelos Generales
    todos: list[dict]
    posts: list[Post]
    model_config = ConfigDict(populate_by_name=True)
    
# [ Modelos de Respuesta ]
class BaseResponse(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    
    @field_serializer('timestamp')
    def serialize_timestamp(self, timestamp: datetime):
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
class UserResponse(BaseResponse):
    body: User
        
class PostsResponse(BaseResponse):
    body: list[Post]

class UserAllDataResponse(BaseResponse):
    body: UserAllData
    