from app import db

class User(db.Model):
    __tablename__="usuarios"

    id = db.Column (db.Integer, primary_key = True)
    username = db.Column (db.String(100), unique = True)
    password = db.Column (db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Produto (db.Model):
    __tablename__="produtos"

    id = db.Column (db.Integer,primary_key = True)
    produto = db.Column (db.String(100))
    valor_unitario = db.Column(db.Float(5,10))
    quantidade = db.Column(db.Integer)
    valor_total = db.Column(db.Float(5,10))

    def __init__(self, produto, valor_unitario, quantidade):
        self.produto = produto
        self.valor_unitario = valor_unitario
        self.valor_total = valor_unitario * quantidade
        self.quantidade = quantidade
