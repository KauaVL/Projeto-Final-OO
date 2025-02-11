# arquivo: main.py

from bottle import Bottle, static_file
from controllers.auth import app as auth_app
from controllers.alunos import app as alunos_app
from controllers.professores import app as professores_app
from controllers.materias import app as materias_app
import threading
import websockets
import asyncio
from websockets.ws_server import handler
from controllers.auth import application as auth_app
from websockets.ws_server import main as start_websocket


app = Bottle()

# Rota para servir arquivos estáticos (CSS, JS)
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

# Rota para servir páginas HTML
@app.route('/')
def index():
    return static_file('index.html', root='views')

@app.route('/alunos')
def alunos_page():
    return static_file('alunos.html', root='views')

# Montando as rotas dos módulos
app.mount("/auth", auth_app)
app.mount("/alunos", alunos_app)
app.mount("/professores", professores_app)
app.mount("/materias", materias_app)

# Iniciando servidor WebSocket
async def start_websocket():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Mantém o servidor rodando

def start_bottle():
    app.run(host='localhost', port=8080, debug=True, reloader=True)

if __name__ == "__main__":
    threading.Thread(target=start_bottle, daemon=True).start()
    asyncio.run(start_websocket())
