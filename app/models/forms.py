from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    
    
class ProdutoForm(FlaskForm):
    produto = StringField('Produto', validators=[DataRequired()])
    valor_unitario = FloatField('Valor_Unitario', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[DataRequired()])
    