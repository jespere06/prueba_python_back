from pydantic import BaseModel, ConfigDict, Field

class Album(BaseModel):
    user_id: int = Field(alias='userId')
    album_id: int = Field(alias='id')
    title: str
    model_config = ConfigDict(populate_by_name=True)
    