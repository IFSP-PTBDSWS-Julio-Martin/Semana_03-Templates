# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request
from flask import redirect
from flask import abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/user/Julio%20Pereira%20Martin/PT3031608/IFSP">Identificação</a></li>
        <li><a href="/contextorequisicao">Contexto da requisição</a></li>
    </ul>
    '''
@app.route('/user/Julio%20Martin')
def user():
    return '''

    '''

@app.route('/rotainexistente')
def erro():
    return '''

    '''
bootstrap = Bootstrap(app)
