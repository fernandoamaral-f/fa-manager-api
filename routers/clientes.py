from fastapi import APIRouter, HTTPException
from schemas import Cliente
from repositories.clientes import ( atualizar_cliente, buscar_cliente_por_id, buscar_todos_clientes, inserir_cliente, deletar_cliente,)

router = APIRouter(prefix="/clientes",tags=["Clientes"])

@router.get("")
def listar_clientes():
    return buscar_todos_clientes()

    
@router.get("/{id}")
def buscar_cliente(id: int):
    cliente = buscar_cliente_por_id(id)

    
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    return cliente

@router.post("", status_code=201)
def cadastrar_cliente(cliente: Cliente):
    novo_id = inserir_cliente(   
            cliente.nome,
            cliente.idade,
            cliente.email,
            cliente.telefone
        )   
    

    novo_cliente = {
        "id": novo_id,
        "nome": cliente.nome,
        "idade": cliente.idade,
        "email": cliente.email,
        "telefone": cliente.telefone
    }

    return novo_cliente

@router.put("/{id}")
def atualizar_cliente_rota(id: int, novos_dados: Cliente):
    linhas_alteradas = atualizar_cliente(
        id,
        novos_dados.nome,
        novos_dados.idade,
        novos_dados.email,
        novos_dados.telefone,
    )
  
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
def deletar_cliente_rota(id: int):    
    linhas_afetadas = deletar_cliente(id)

    if linhas_afetadas == 0:   
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return {"mensagem": "Cliente deletado com sucesso"}
