from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Fa Manager V2"}


def test_buscar_cliente_com_id_invalido():
    response = client.get("/clientes/abc")

    assert response.status_code == 422


def test_buscar_cliente_inexistente():
    response = client.get("/clientes/999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Cliente não encontrado"}


def test_cadastrar_cliente_com_idade_invalida():
    response = client.post(
        "/clientes",
        json={
            "nome": "Cliente Teste",
            "idade": 150,
            "email": "teste@email.com",
            "telefone": "47999999999"
        }
    )

    assert response.status_code == 422