#rotas

from app import app # importando a variável app que está dentro do módulo app

#Função de definição de Rota da página
@app.route("/")
def index():
    return "Hello"