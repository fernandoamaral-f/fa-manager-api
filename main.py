from database import conectar, criar_tabela
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Cliente(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nome: str = Field(min_length=2, max_length=100)
    idade: int = Field(gt=0, le=120)
    email: EmailStr
    telefone: str


app = FastAPI()

criar_tabela()

@app.get("/")
def home():
    return {"mensagem": "Fa Manager V2"}

@app.get("/clientes",)
def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    clientes_convertidos = []

    for cliente in clientes:
        clientes_convertidos.append(dict(cliente))


    conexao.close()

    return clientes_convertidos


@app.get("/clientes/{id}")
def buscar_cliente (id: int):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE id = ?",
        (id,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return dict(cliente)



@app.post("/clientes", status_code=201)
def cadastrar_cliente(cliente: Cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """ INSERT INTO clientes (nome, idade, email, telefone)
        VALUES (?, ?, ?, ?) """,

        (   
            cliente.nome,
            cliente.idade,
            cliente.email,
            cliente.telefone
        )
    
    )

    conexao.commit()

    novo_id = cursor.lastrowid

    novo_cliente = {
        "id": novo_id,
        "nome": cliente.nome,
        "idade": cliente.idade,
        "email": cliente.email,
        "telefone": cliente.telefone
    }

    conexao.close()

    return novo_cliente

    
@app.put("/clientes/{id}")
def atualizar_cliente(id: int, novos_dados: Cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """ UPDATE clientes SET nome = ?, idade = ?, email = ?, telefone = ? WHERE id = ? """,

        (
            novos_dados.nome,
            novos_dados.idade,
            novos_dados.email,
            novos_dados.telefone,
            id
            
        )
    )

    conexao.commit()

    linhas_alteradas = cursor.rowcount

    conexao.close()

    if linhas_alteradas == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {
        "id": id,
        "nome": novos_dados.nome,
        "idade": novos_dados.idade,
        "email": novos_dados.email,
        "telefone": novos_dados.telefone
    }
     
      
      
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
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """ DELETE FROM clientes WHERE id = ?""",
        (id,)
    )

    conexao.commit()

    linhas_afetadas = cursor.rowcount

    conexao.close()

    if linhas_afetadas == 0:   
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {"mensagem": "Cliente deletado com sucesso"}
