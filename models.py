from typing import List, Optional
from pydantic import BaseModel

class University(BaseModel):
    name: str
    country: str
    domains: List[str]
    web_pages: List[str]

