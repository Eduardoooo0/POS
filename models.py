from pydantic import BaseModel
from typing import List

class University(BaseModel):
    name: str
    country: str
    domains: List[str]
    web_pages: List[str]
