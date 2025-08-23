# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request
from flask import redirect
from flask import abort

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

@app.route('/user/<name>/<prontuario>/<instituicao>')
def user(name, prontuario, instituicao):
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Aluno: {name}</h2>
    <h2>Prontuário: {prontuario}</h2>
    <h2>Instituição: {instituicao}</h2>
    <br>
    <a href="/">Voltar</a>
    '''

@app.route('/contextorequisicao')
def req():
    cont_req = request.headers.get('User-Agent')
    ip_usuario = request.remote_addr
    host = request.host
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {cont_req}</h2>
    <h2>O IP do cumputador remoto é: {ip_usuario}</h2>
    <h2>O host da aplicação é: {host}</h2>
    <br>
    <a href="/">Voltar</a>
    '''

''' @app.route('/codigostatusdiferente')
def status():
    return '<p>Bad request</p>'

@app.route('/objetoresposta')
def obj():
    return '<h1>This document carries a cookie!</h1>'

@app.route('/redirecionamento')
def redirecionar():
    return redirect('https://ptb.ifsp.edu.br/')

@app.route('/abortar')
def abortar():
    return abort(404)
'''
