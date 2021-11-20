from app import app # importando a variável app que está dentro do módulo app
from flask import render_template

from app import app
from app.models.forms import UserForm

#Função de definição de Rota da página
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/login")
def login():
    form = UserForm()
    # TODO CRIAR AUTENTICAÇÃO APÓS CRIAÇÃO DO BANCO DE DADOS
    return render_template("login.html", form=form)