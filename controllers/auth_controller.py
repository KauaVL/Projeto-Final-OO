from flask import Blueprint, render_template, request, session, redirect
import sqlite3

# Cria o Blueprint para autenticação
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        # Conecta ao banco de dados
        conn = sqlite3.connect('escola.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
        user_data = cursor.fetchone()
        conn.close()
        
        if user_data:
            session['user_id'] = user_data[0]
            session['tipo'] = user_data[4]  # admin, professor ou aluno
            return redirect('/dashboard')
        return "Credenciais inválidas!"
    return render_template('login.html')  # Renderiza o template login.html

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


