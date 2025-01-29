# Pucly: Um Projeto em Django

## Configuração do Ambiente
Clone o repositório ou extraia o zip baixado e abra a pasta do projeto na sua IDE.

Abra o terminal e navegue até a pasta correta.

Crie um ambiente virtual Python (venv) usando o comando:
```bash
python -m venv venv
```

Não esqueça de baixar a versão mais recente do Python se não tiver. Apos a criação da venv será possivel ativa-la.

## Ativando a venv:

No Windows:
```bash
.\.venv\Scripts\activate
```
No macOS/Linux:
```bash
source .venv/bin/activate
```
Para desativar a venv basta usar o comando:
```bash
deactivate
```

A utilização de uma venv é aconselhável para isolar as dependências do projeto, evitando conflitos entre diferentes projetos e facilitando a distribuição.

## Instale o gerenciador de pacotes Poetry:

```bash
pip install poetry
```
Instale as dependências do projeto com o comando:

```bash
poetry install
```
Todos os pacotes usados no projeto serão instalados.

## Executando o Projeto
Com o diretório do projeto aberto na IDE e a venv ativada, antes de rodar o projeto pela primeira vez utilize o comando:

```bash
python manage.py makemigrations
```
Seguido de:

```bash
python manage.py migrate
```
Finalmente, para iniciar o projeto, execute:

```bash
python manage.py runserver
```

O acesso ao site estará disponível na porta padrão: http://127.0.0.1:8000/ .

