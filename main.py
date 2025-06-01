from fastapi import FastAPI
from api import router

app = FastAPI(
    title="UniSearch",
    description="API para busca de universidades no mundo todo",
    version="1.0"
)

app.include_router(router)
