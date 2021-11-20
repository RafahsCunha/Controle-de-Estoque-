from app import db

class User(db.Model):
    __tablename__="usuarios"

    id = db.Coumn (db.integer, primary_key = True)
    username = db.Column (db.String(100), unique = True)
    password = db.Column (db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


    class Produto (db.Model):
        __tablename__="produtos"

        id = db.Column (db.integer,primary_key = True)
        produto = db.Column (db.String(100))
        preco = db.Column(db.Float(5,10))
        estoque_atual = db.Column(db.integer)
        estoque_minimo = db.Column(db.integer)

    def __init__(self, produto, preco, estoque_atual, estoque_minimo):
        self.produto = produto
        self.preco = preco
        self.estoque_atual = estoque_atual
        self.estoque_minimo = estoque_minimo




