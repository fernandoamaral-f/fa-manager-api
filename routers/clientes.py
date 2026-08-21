from fastapi import APIRouter, HTTPException
from database import conectar
from schemas import Cliente

router = APIRouter(prefix="/clientes",tags=["Clientes"])

@router.get("")
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


@router.get("/{id}")
def buscar_cliente(id: int):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM clientes WHERE id = ?",
        (id,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return dict(cliente)

@router.post("", status_code=201)
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

@router.put("/{id}")
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
     

@router.delete("/{id}")
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
