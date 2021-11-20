from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
    
class Produto:
    produto = StringField('produto', validators=[DataRequired()])
    valor_unitario = FloatField('valor_unitario', validators=[DataRequired()])
    quantidade = IntegerField('quantidade', validators=[DataRequired()])
    