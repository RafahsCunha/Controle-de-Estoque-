from app import app # importando a variável app que está dentro do módulo app
from flask import render_template, request, redirect, url_for

from app import app, db, login_manager
from app.models.forms import UserForm, ProdutoForm
from app.models.tables import Produto, User
from flask_login import login_user, login_required, current_user, logout_user

#Função de definição de Rota da página
@app.route("/")
@login_required
def index():
    produtos = Produto.query.all()
    print("PRODUTOS: ", produtos)
    # FALTA PEGAR OS PRODUTOS E INSERIR NA HOME
    return render_template("home.html", produtos=produtos)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = UserForm()
    
    if request.method == "POST":
        if form.username.data == "admin" and form.password.data == "admin":
            user = User.query.filter_by(username=form.username.data).first()
            login_user(user)
            return redirect(url_for("index"))
    
    return render_template("login.html", form=form)

@app.route("/cadastrodeproduto", methods=['GET', 'POST'])
def produto():
    form = ProdutoForm()
    
    if request.method == "POST":
        if form.validate():
            new_produto = Produto(
                produto=form.produto.data,
                valor_unitario=form.valor_unitario.data, 
                quantidade=form.quantidade.data
            )
            db.session.add(new_produto)
            db.session.commit()

    return render_template("cadastrodeproduto.html", form=form)

