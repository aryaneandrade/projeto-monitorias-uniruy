# Plataforma de Monitorias Acadêmicas – UniRuy Wyden

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-darkgreen?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-316192?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-Orchestration-1D63ED?logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Web_Server-009639?logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI_Server-499848)

Aplicação Django para gestão de monitorias acadêmicas com painel de monitores, cadastro de inscrições e controle de vagas.

## Visão geral

O projeto oferece:

- autenticação de usuários com email ou username;
- cadastro, edição e exclusão de monitorias;
- controle de inscrições e limite de vagas;
- painel restrito para cada monitor;
- execução oficial via Docker Compose com PostgreSQL, Gunicorn e Nginx.

## Arquitetura

O sistema utiliza a seguinte pilha:

- Django 6
- PostgreSQL
- Docker
- Docker Compose
- Gunicorn
- Nginx

## Estrutura do repositório

- `app/` – configuração do Django, URLs e templates principais
- `contas/` – autenticação e registro de usuários
- `monitorias/` – models, views, forms e templates de monitorias e inscrições
- `static/` – CSS e arquivos estáticos do frontend
- `docker-compose.yml` – ambiente local
- `docker-compose.prod.yml` – ambiente de produção
- `docs/` – documentação adicional do projeto
- `.env.example` – modelo de variáveis para ambiente local
- `.env.example-prod` – modelo de variáveis para produção

## Pré-requisitos

- Docker
- Docker Compose

## Clonando o repositório

```bash
git clone https://github.com/aryaneandrade/projeto-monitorias-uniruy.git
cd projeto-monitorias-uniruy
```

## Configuração do ambiente local

Para executar localmente, crie o arquivo de ambiente a partir do modelo local:

```bash
cp .env.example .env
```

O arquivo `.env.example` é usado para execução local e pode ser ajustado conforme necessário.

## Execução local

O fluxo oficial de execução local é:

```bash
docker compose up -d --build
```

Os serviços são iniciados automaticamente e incluem:

- PostgreSQL
- Django
- Gunicorn
- Nginx

O entrypoint do container já aplica migrações e coleta os arquivos estáticos automaticamente.

## Acessando o sistema

- Página inicial: `http://127.0.0.1:8080/`
- Portal de monitorias: `http://127.0.0.1:8080/monitorias/`
- Django Admin: `http://127.0.0.1:8080/admin/`

## Administração

Para criar um superusuário pelo container:

```bash
docker compose exec web python manage.py createsuperuser
```

## Testes

Para executar a suíte de testes via Docker:

```bash
docker compose exec web python manage.py test
```

## Deploy de produção

O projeto suporta execução em nuvem utilizando Docker Compose.

Para preparar o ambiente de produção, utilize o modelo de variáveis de ambiente de produção:

```bash
cp .env.example-prod .env
```

Ajuste os valores em `.env` conforme o ambiente de produção.

## Documentação

- `docs/` – documentação adicional, relatórios e materiais de apoio

## Observações

- A execução oficial do projeto é feita via Docker Compose.
- As configurações de ambiente são definidas em `.env`.
- O container aplica migrações e coleta arquivos estáticos automaticamente.
