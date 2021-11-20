from app import app # importando a variável app que está dentro do módulo app
from flask import render_template

from app import app
from app.models.forms import UserForm, ProdutoForm

#Função de definição de Rota da página
@app.route("/")
def index():
    return render_template("home.html")


@app.route("/login")
def login():
    form = UserForm()
    return render_template("login.html", form=form)

@app.route("/cadastrodeproduto")
def produto():
    form = ProdutoForm()
    return render_template("cadastrodeproduto.html", form=form)

