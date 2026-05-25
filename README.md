# Plataforma de Monitorias Acadêmicas – UniRuy Wyden

Aplicação Django para gestão de monitorias acadêmicas, com cadastro de monitores, divulgação de vagas e controle de inscrições.

## Visão geral

Sistema web com painel de monitores e portal público de monitorias. O projeto oferece:

- autenticação de usuários;
- cadastro e edição de monitorias;
- gestão de inscrições e vagas;
- painel restrito para monitores.

## Funcionalidades principais

- listagem pública de monitorias;
- cadastro e login de monitores;
- painel privado para gerenciamento de monitorias;
- criação, edição e exclusão de monitorias;
- controle de inscrições com limite de vagas;
- proteção de acesso por proprietário.

## Tecnologias

- Python
- Django 6
- PostgreSQL
- Docker & Docker Compose
- Bootstrap 5

## Estrutura principal

- `app/` – configuração do projeto, URLs e templates globais
- `contas/` – autenticação e registro
- `monitorias/` – gestão de monitorias e inscrições
- `static/` – assets de CSS e imagens
- `docker-compose.yml` – ambiente local
- `docker-compose.prod.yml` – ambiente de produção

## Instalação local

```bash
git clone https://github.com/aryaneandrade/projeto-monitorias-uniruy.git
cd projeto-monitorias-uniruy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/monitorias/`

## Execução com Docker

```bash
docker compose up -d --build
```

Acesse o serviço local configurado em `http://127.0.0.1:8080/`.

## Deploy AWS

O ambiente de produção utiliza:

- Amazon EC2
- Amazon RDS PostgreSQL
- Nginx
- Gunicorn
- Docker Compose

As configurações de ambiente são realizadas via arquivo `.env`

## Observações

- Projeto configurado para PostgreSQL em `app/settings.py`.
- Interface administrativa disponível em `/admin/`
- Ambiente preparado para deploy em produção com Docker
