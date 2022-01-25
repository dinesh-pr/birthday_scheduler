import datetime
from xmlrpc.client import DateTime
from pydantic import BaseModel
from typing import List,Optional


class register(BaseModel):
    name:str
    email:str
    password:str
    createdAt=DateTime
    updatedAt=DateTime
    class config():
        orm_mode=True

class login(BaseModel):
    username:str
    password:str

class upload(BaseModel):
    name:str
    email:str
    password:str
    class config():
        orm_mode=True

class update(BaseModel):
    name:str
    number:int
    birthday_date:datetime.date
    class config:
        orm_mode=True
    class Config:
        arbitrary_types_allowed = True


class text(BaseModel):
    text:str
    
    class config:
        orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []