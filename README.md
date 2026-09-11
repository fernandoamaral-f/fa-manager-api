# FA Manager API

API backend do **FA Manager**, um sistema em desenvolvimento para gerenciamento de clientes e operações de uma empresa de serviços.

O projeto está sendo desenvolvido como aplicação prática dos meus estudos em desenvolvimento backend, com foco em **Python, FastAPI, APIs REST, banco de dados, testes, organização de código e arquitetura backend**.

## Status do projeto

🚧 **Em desenvolvimento**

Atualmente, a API já possui a estrutura inicial para gerenciamento de clientes e continua evoluindo com novas funcionalidades e melhorias de arquitetura.

## Funcionalidades implementadas

- CRUD de clientes
- Persistência de dados com SQLite
- Validação de dados com Pydantic
- Separação de rotas e camada de repositório
- Configurações por ambiente com `pydantic-settings`
- Banco isolado para execução de testes
- Testes automatizados do CRUD
- Arquivo `.env.example` para configuração do ambiente

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- Pydantic
- pydantic-settings
- Git
- GitHub

## Estrutura atual

```text
fa-manager-api/
├── repositories/     # Acesso e persistência de dados
├── routers/          # Rotas da API
├── tests/            # Testes automatizados
├── .env.example      # Exemplo de configuração de ambiente
├── .gitignore
├── config.py         # Configurações da aplicação
├── database.py       # Configuração do banco de dados
├── main.py           # Inicialização da aplicação
├── requirements.txt  # Dependências do projeto
└── schemas.py        # Schemas e validação de dados
