from fastapi.testclient import TestClient

from main import app

import pytest
import database

client = TestClient(app)

@pytest.fixture(autouse=True)
def banco_de_teste(tmp_path, monkeypatch):
    caminho_teste = tmp_path / "teste.db"

    monkeypatch.setattr(
        database,
        "CAMINHO_BANCO",
        str(caminho_teste)
    )

    database.criar_tabela()

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


def test_cadastrar_cliente():
    response = client.post(
        "/clientes",
        json={
            "nome": "Fernando Teste",
            "idade": 37,
            "email": "fernando.teste@email.com",
            "telefone": "47999999999"
        }
    )

    assert response.status_code == 201

    cliente_criado = response.json()

    assert cliente_criado["nome"] == "Fernando Teste"
    assert cliente_criado["idade"] == 37

    novo_id = cliente_criado["id"]

    response_get = client.get(f"/clientes/{novo_id}")

    assert response_get.status_code == 200


def test_atualizar_cliente():
    response_post = client.post(
        "/clientes",
        json={
            "nome": "Cliente Original",
            "idade": 30,
            "email": "original@email.com",
            "telefone": "47999999999"
        }
    )

    novo_id = response_post.json()["id"]

    response_put = client.put(
        f"/clientes/{novo_id}",
        json={
            "nome": "Cliente Atualizado",
            "idade": 31,
            "email": "atualizado@email.com",
            "telefone": "47988888888"
        }
    )

    assert response_put.status_code == 200

    response_get = client.get(f"/clientes/{novo_id}")

    assert response_get.status_code == 200
    assert response_get.json()["nome"] == "Cliente Atualizado"
    assert response_get.json()["idade"] == 31

def test_deletar_cliente():
    response_post = client.post(
        "/clientes",
        json={
            "nome": "Cliente Para Deletar",
            "idade": 40,
            "email": "deletar@email.com",
            "telefone": "47977777777"
        }
    )

    novo_id = response_post.json()["id"]

    response_delete = client.delete(
        f"/clientes/{novo_id}"
    )

    assert response_delete.status_code == 200

    response_get = client.get(
        f"/clientes/{novo_id}"
    )

    assert response_get.status_code == 404