from pydantic import BaseModel, ConfigDict, Field

class Post(BaseModel):
    user_id: int = Field(alias='userId')
    post_id: int = Field(alias='id')
    title: str
    body: str
    model_config = ConfigDict(populate_by_name=True)