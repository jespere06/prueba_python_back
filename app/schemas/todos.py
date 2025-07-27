from pydantic import BaseModel, ConfigDict, Field

class Todos(BaseModel):
    user_id: int = Field(alias='userId')
    todos_id: int = Field(alias='id')
    title: str
    completed: bool
    model_config = ConfigDict(populate_by_name=True)
    