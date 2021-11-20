# Iniciação do módulo app - OBS módulo principal

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask (__name__)

app.config.from_object('config')

app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return tables.User.query.filter_by(id=user_id).first()

from app.models import tables, forms
from app.controllers import default










