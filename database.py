from contextlib import ContextDecorator
import sqlite3

def conectar():
    conexao = sqlite3.connect("fa_manager.db")
    conexao.row_factory = sqlite3.Row
    return conexao  

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, email TEXT, telefone TEXT)""")
    
    conexao.close()


