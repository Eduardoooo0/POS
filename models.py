from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class University(BaseModel):
    name: str
    country: str
    domains: List[str]
    web_pages: List[str]

class Favorite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    country: str
    domains: str  
    web_pages: str

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str