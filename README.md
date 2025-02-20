# Sistema de Gerenciamento Acadêmico

## Descrição
Sistema desenvolvido para a disciplina de Orientação a Objetos da Universidade de Brasília (UnB), ministrada pelo professor Henrique. O projeto implementa um sistema de gerenciamento acadêmico com funcionalidades para administradores, professores e alunos.

## Funcionalidades Principais

### Administrador
- Gerenciamento completo de usuários (CRUD)
  - Criar novos usuários (professores/alunos)
  - Visualizar todos os usuários
  - Atualizar informações de usuários
  - Remover usuários
- Gerenciamento completo de turmas (CRUD)
  - Criar novas turmas
  - Visualizar todas as turmas
  - Atualizar informações de turmas
  - Remover turmas
- Gestão de matrículas
  - Adicionar alunos às turmas
  - Remover alunos das turmas
  - Visualizar alunos matriculados

### Professores
- Visualização das turmas ministradas
- Acesso à lista de alunos matriculados

### Alunos
- Visualização das turmas matriculadas

## Tecnologias Utilizadas
- Python 3.x
- Flask (Framework Web)
- SQLAlchemy (ORM)
- SQLite (Banco de Dados)
- HTML/CSS
- JavaScript
- Docker

## Pré-requisitos

- Docker
- Docker Compose

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Construir a imagem e rodar o container:
```bash
docker-compose up --build
```

3.Acessar a aplicação:
```bash
http://localhost:5000
```

3.Desligar container:
```bash
docker-compose down
```

## Estrutura do Projeto
```
projetofinal_OO/
├── app.py
├── static/
│   └── css/
│       ├── CRUD_turmas/
│       └── CRUD_usuarios/
├── templates/
│   ├── admin/
│   │   ├── CRUD_turmas/
│   │   └── CRUD_usuarios/
│   ├── dashboard.html
│   ├── home.html
│   ├── login.html
│   └── signup.html
└── requirements.txt
│── docker-compose.yml
│── Dockerfile
│── data/

```

## Credenciais de Administrador
```
Email: admin@admin.com
Senha: admin123
```

## Modelos de Dados

### User
- email (PK)
- nome
- cargo (Professor/Aluno)
- senha

### Turma
- codigo_disciplina (PK)
- nome
- professor_email (FK)
- ano
- semestre

## Contribuidores
- Kaua Vale Leão
- Arthur Henrique Vieira
- Jânio Lucas Pereira Carrilho

## Professor Orientador
Prof. Henrique - Universidade de Brasília (UnB)

