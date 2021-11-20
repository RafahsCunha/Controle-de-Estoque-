# Iniciação do módulo app - OBS módulo principal

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)
app.config.from_object('config')

app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import tables, forms
from app.controllers import default










