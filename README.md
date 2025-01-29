# Pucly: Um Projeto em Django

## Sobre a Pucly

Trabalho realizado no segundo período de Ciência da Computação na disciplina INF1039, Projetos: Aplicações Interativas, da PUC-RJ, ministrada pelo professor Adriano Francisco Branco.

Pucly surgiu da ideia da criação de um site onde estudantes da PUC-RJ, de todos os cursos, poderiam postar dúvidas e responder às de outros colegas. Além de divulgar gabaritos para listas de exercícios. Criando assim um ambiente de cooperação onde estudantes poderiam buscar ajuda para sanar suas próprias dúvidas, ou praticar seu conhecimento ajudando outros.

A implementação foi feita utilizando o framework do Django e ao longo do período foram introduzidos ao site diversos recursos com objetivo didático, como sistema de registro/login com verificação real por e-mail, perfis pessoais e personalização, sistema de ranking, notificações em tempo real e como parte principal do site, o sistema de criação de dúvidas e a possibilidade da adição de respostas a essas dúvidas, entre muitos outros. 

## Configuração do Ambiente
Clone o repositório ou extraia o zip baixado e abra a pasta do projeto na sua IDE.

Abra o terminal e navegue até a pasta correta.

Crie um ambiente virtual Python (venv) usando o comando:
```bash
python -m venv venv
```

Não esqueça de baixar a versão mais recente do Python se não tiver. Apos a criação da venv será possivel ativa-la.

## Ativando a venv

No Windows:
```bash
venv\Scripts\activate
```
No macOS/Linux:
```bash
source venv/bin/activate
```
Para desativar a venv basta usar o comando:
```bash
deactivate
```

A utilização de uma venv é aconselhável para isolar as dependências do projeto, evitando conflitos entre diferentes projetos e facilitando a distribuição.

## Instale o gerenciador de pacotes Poetry

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

O acesso ao site estará disponível em seu navegador na porta padrão: http://127.0.0.1:8000/ .

