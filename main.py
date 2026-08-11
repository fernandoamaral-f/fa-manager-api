from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

clientes =[
    {   
        "id": 1,
        "nome": "João",
        "idade": 30,
        "email": "joao@example.com",
        "telefone": "1234567890"
}

]



class Cliente(BaseModel):
    nome: str
    idade: int
    email: str
    telefone: str


app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Fa Manager V2"}

@app.get("/clientes")
def listar_clientes():
    return clientes

@app.get("/clientes/{id}")
def buscar_cliente (id: int):
    for cliente in clientes:
        if cliente["id"] == id:
         return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.post("/clientes")
def cadastrar_cliente(cliente: Cliente):
    novo_cliente = {    
        "id": len(clientes) + 1,
        "nome": cliente.nome,
        "idade": cliente.idade,
        "email": cliente.email,
        "telefone": cliente.telefone
    }
    clientes.append(novo_cliente)
    return novo_cliente
 
@app.put("/clientes/{id}")
def atualizar_cliente(id: int, novos_dados: Cliente):
    for cliente in clientes:
        if cliente["id"] == id:
            cliente["nome"] = novos_dados.nome
            cliente["idade"] = novos_dados.idade
            cliente["email"] = novos_dados.email
            cliente["telefone"] = novos_dados.telefone
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.delete("/clientes/{id}")
def deletar_cliente(id: int):
    for cliente in clientes:
        if cliente["id"] == id:
            clientes.remove(cliente)
            return {"mensagem": "Cliente deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

