# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/user/<nome>')
def user(nome):
    return render_template('user.html', nome=nome)

@app.route('/rotainexistente')
def erro():
    return render_template('404.html') 
