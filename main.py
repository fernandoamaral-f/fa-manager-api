from database import criar_tabela
from fastapi import FastAPI
from routers.clientes import router as clientes_router


app = FastAPI()

app.include_router(clientes_router)


criar_tabela()

@app.get("/")
def home():
    return {"mensagem": "Fa Manager V2"}
    

