from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
    
class Produto:
    produto = StringField('produto', validators=[DataRequired()])
    preco = FloatField('preco', validators=[DataRequired()])
    estoque_atual = IntegerField('estoque_atual', validators=[DataRequired()])
    estoque_minimo = IntegerField('estoque_atual', validators=[DataRequired()])
    