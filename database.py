import sqlite3

from config import settings



CAMINHO_BANCO = settings.caminho_banco

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao  

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, email TEXT, telefone TEXT)""")
    
    conexao.close()


