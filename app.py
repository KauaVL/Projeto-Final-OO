from flask import Flask, redirect
from controllers.auth_controller import auth_bp

app = Flask(__name__)
app.secret_key = 'supersenha'

# Registra o Blueprint de autenticação
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)