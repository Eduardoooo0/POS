from fastapi import FastAPI

app = FastAPI()

@app.get('/teste')
def teste():
    return 'teste'