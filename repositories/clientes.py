from sqlite3 import Cursor
from database import conectar

def buscar_todos_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM clientes""")
    clientes = cursor.fetchall()

    clientes_convertidos = []

    for cliente in clientes:
        clientes_convertidos.append(dict(cliente))

    conexao.close()

    return clientes_convertidos


def buscar_cliente_por_id(id: int):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute( """SELECT * FROM clientes WHERE id = ?""",
    (id,)
    )

    cliente = cursor.fetchone()

    conexao.close()

    if cliente is None:
        return None

    return dict(cliente)


def inserir_cliente(nome, idade, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""INSERT INTO clientes (nome, idade, email, telefone)
        VALUES (?, ?, ?, ?)
        """,
        (
            nome,
            idade,
            email,
            telefone
        )
    )

    conexao.commit()

    novo_id = cursor.lastrowid

    conexao.close()

    return novo_id


def atualizar_cliente(id, nome, idade, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""UPDATE clientes SET nome = ?, idade = ?, email = ?, telefone = ?
        WHERE id = ?
        """,
        (
            nome,
            idade,
            email,
            telefone,
            id
        )
    )

    conexao.commit()

    linhas_alteradas = cursor.rowcount

    conexao.close()

    return linhas_alteradas

def deletar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id,)
    )

    conexao.commit()

    linhas_afetadas = cursor.rowcount

    conexao.close()

    return linhas_afetadas