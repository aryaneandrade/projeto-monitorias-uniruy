# Plataforma de Monitorias Acadêmicas – UniRuy Wyden

Plataforma web construída em Django para gerenciamento de monitorias acadêmicas. A aplicação centraliza a divulgação de monitorias, permite cadastro de monitores, inscrições de alunos e controle de vagas.

---

## Visão Geral

A solução é composta por dois aplicativos Django principais:

- `contas`: autenticação de usuários, registro e acesso ao painel do monitor.
- `monitorias`: cadastro, edição, exclusão e listagem de monitorias; gerenciamento de inscrições; controle de capacidade.

A arquitetura segue o padrão Django MVC, com:

- `app/`: configuração do projeto Django, URLs e templates globais.
- `monitorias/`: lógica de negócio para monitorias, inscrições, categorias e benefícios.
- `contas/`: formulários e views de autenticação.
- `static/`: recursos estáticos de CSS e imagens.

---

## Funcionalidades Principais

- Página pública de listagem de monitorias em `/monitorias/`.
- Pesquisa por título e filtro por categoria na listagem pública.
- Cadastro e login de usuários para monitores.
- Painel privado do monitor em `/painel/`.
- Criação, edição e exclusão de monitorias próprias.
- Visualização de inscritos por monitoria.
- Registro de inscrições públicas com validação de e-mail único por monitoria.
- Controle de vagas através da propriedade `Monitoria.vagas` e filtro de lotação.
- Proteção de edição/exclusão para que apenas o proprietário da monitoria possa gerenciar seus dados.

---

## Regras de Negócio

- Monitores devem estar autenticados para criar, editar, excluir monitorias e acessar o painel.
- Um monitor não pode inscrever-se em sua própria monitoria.
- Cada inscrição é vinculada a uma `Monitoria` e contém `nome`, `email` e `telefone`.
- O e-mail de inscrição deve ser único para cada monitoria (`UniqueConstraint` em `Inscricao`).
- Uma monitoria lota quando o total de inscrições atinge o número de vagas configurado.
- Categorias e benefícios são referências obrigatórias para monitorias e devem ser preenchidas antes da criação.

---

## Estrutura do Projeto

```text
projeto-monitorias-uniruy/
├── app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── templates/
│       ├── base.html
│       └── home.html
├── contas/
│   ├── __init__.py
│   ├── forms.py
│   ├── views.py
│   └── templates/
│       ├── login.html
│       └── registro.html
├── monitorias/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── criar_monitoria.html
│       ├── editar_monitoria.html
│       ├── excluir_monitoria.html
│       ├── inscricao.html
│       ├── inscritos_monitoria.html
│       ├── monitorias.html
│       └── painel_monitor.html
├── static/
│   ├── css/
│   └── img/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Tecnologias Utilizadas

- Django 6.0.5
- Python (versão compatível com Django 6)
- PostgreSQL (configuração padrão em `app/settings.py`)
- psycopg2-binary
- Pillow
- Bootstrap 5 (via CDN)
- Font Awesome (via CDN)

---

## Instalação

```bash
git clone https://github.com/aryaneandrade/projeto-monitorias-uniruy.git
cd projeto-monitorias-uniruy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuração do banco de dados

O projeto está configurado para PostgreSQL em `app/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'monitorias',
        'USER': 'postgres',
        'PASSWORD': 'postgres123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Atualize esses valores conforme o ambiente local.

---

## Execução

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse a aplicação em `http://127.0.0.1:8000/monitorias/`.

---

## Administração

A interface administrativa do Django está disponível em `/admin/`.

Modelos registrados:

- `Monitoria`
- `Categoria`
- `Beneficio`
- `Inscricao`

Use o admin para gerenciar categorias e benefícios antes de criar monitorias.

---

## Observações

- O projeto está configurado para PostgreSQL e o deploy atual usa Gunicorn com Nginx.
- `db.sqlite3` está presente localmente como artefato de desenvolvimento, mas não é usado pela configuração Docker atual.
- O sistema não implementa integrações externas de pagamento, mensageria ou APIs de terceiros.
