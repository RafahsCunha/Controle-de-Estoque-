from app import db

class User(db.Model):
    __tablename__="usuarios"

    id = db.Column (db.Integer, primary_key = True)
    username = db.Column (db.String(100), unique = True)
    password = db.Column (db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated
    
    def is_active(self):
        """True, as all users are active."""
        return True

class Produto (db.Model):
    __tablename__="produtos"

    id = db.Column (db.Integer,primary_key = True)
    produto = db.Column (db.String(100))
    valor_unitario = db.Column(db.Float(5,10))
    quantidade = db.Column(db.Integer)
    valor_unitario = db.Column(db.Float(5,10))

    def __init__(self, produto, preco, valor_unitario, quantidade):
        self.produto = produto
        self.preco = preco
        self.valor_unitario = valor_unitario
        self.valor_total = self.get_valor_total(valor_unitario, quantidade)
        self.quantidade = quantidade
        
    def get_valor_total(self, valor_unitario, quantidade):
        return valor_unitario * quantidade
    




