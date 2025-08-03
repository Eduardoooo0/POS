from fastapi import FastAPI
from api import router
from db import create_db

app = FastAPI(
    title="UniSearch",
    description="API para busca de universidades no mundo todo",
    version="1.0"
)

create_db() 
app.include_router(router)
