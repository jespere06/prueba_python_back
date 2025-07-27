from pydantic import BaseModel, ConfigDict, EmailStr, Field

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
    website: str
    company: Company
    model_config = ConfigDict(populate_by_name=True)
