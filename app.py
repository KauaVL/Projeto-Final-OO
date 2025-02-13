from flask import Flask, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'supersenha'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(150), unique=True, nullable=False, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(150), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cargo = request.form['cargo']
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email já registrado. Tente fazer login.')
            return redirect(url_for('login'))
        else:
            try:
                new_user = User(nome=nome, email=email, senha=senha, cargo=cargo)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('login'))
            except Exception:
                db.session.rollback()
                flash('Erro ao realizar cadastro. Tente novamente.')
                return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = User.query.filter_by(email=email).first()
        if user and user.senha == senha:
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/admin/users', methods=['GET'])
def read_users():
    users = User.query.all()
    return render_template('admin/read.html', users=users)

@app.route('/admin/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cargo = request.form['cargo']
        new_user = User(nome=nome, email=email, senha=senha, cargo=cargo)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário criado com sucesso!')
        return redirect(url_for('read_users'))
    return render_template('admin/create.html')

@app.route('/admin/users/update/<email>', methods=['GET', 'POST'])
def update_user(email):
    user = User.query.get_or_404(email)
    if request.method == 'POST':
        user.nome = request.form['nome']
        user.senha = request.form['senha']
        user.cargo = request.form['cargo']
        db.session.commit()
        flash('Usuário atualizado com sucesso!')
        return redirect(url_for('read_users'))
    return render_template('admin/update.html', user=user)

@app.route('/admin/users/delete/<email>', methods=['GET', 'POST'])
def delete_user(email):
    user = User.query.get_or_404(email)
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash('Usuário deletado com sucesso!')
        return redirect(url_for('read_users'))
    return render_template('admin/delete.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)