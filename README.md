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

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o aplicativo:
```bash
python app.py
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
└── users.db
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

