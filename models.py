from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class User(BaseModel):
    user_id: int
    albums: list[dict]
    todos: list[dict]
    posts: list[dict]
    model_config = ConfigDict(populate_by_name=True)

class Post(BaseModel):
    user_id: int
    post_id: int = Field(alias='id')
    title: str
    body: str
    model_config = ConfigDict(populate_by_name=True)
    
class FetchEngineResponse(BaseModel):
    body: list[Post] | User = Field(default=...)
    timestamp: datetime = Field(default_factory=datetime.now)
    