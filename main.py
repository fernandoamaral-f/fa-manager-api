
from contextlib import asynccontextmanager
from database import criar_tabela
from fastapi import FastAPI
from routers.clientes import router as clientes_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_tabela()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(clientes_router)

@app.get("/")
def home():
    return {"mensagem": "Fa Manager V2"}
    

