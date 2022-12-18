from flask import Flask, request
from flask_restful import Resource, Api
import json

#atravez desse exercicio entendi a importancia dos padrões em todos os projetos, 
#atravez de uma arquitetura é possivel tornar o codigo mais organizado e de facil compreenção. 
#primeira ApiRestfull.

app = Flask(__name__)
api = Api(app)

Habilidades = ['Python','Flask','Pandas']
#Class que possui metodos que ler,altera e apaga habilidades selecionadas pelo usuario.
class Desenvolvedor(Resource):
    def get(self,id):
        if Habilidades:
            try:
                skilll = Habilidades[id]
            except IndexError:
                return {"Aviso": "Not Found", "Menssagem": "Usuario não encontrado"}
        return skilll
    
    def put(self,id):
        skil = json.loads(request.data)
        Habilidades[id] = skil
        return skil
    
    def delete(self,id):
        Habilidades.pop(id)
        return {"Aviso": "Sucesso", "Menssagem": "Habilidade excluida com sucesso!"}

#Class que possui metodos de adicionar novas habilidades e lista todas elas.   
class SelectandInclude(Resource):
    def post(self):
        
        if json.loads(request.data) not in Habilidades:
            skill = json.loads(request.data)
            Habilidades.append(skill)
            return({"Aviso":"Sucesso!", "Messagem":"Habilidade Registrada com Sucesso!"})
        return {"Aviso": "Erro!", "Menssagem": "Habilidade ja Existe!"}
    
    def get(self):
        return Habilidades

    
# Define Rotas
api.add_resource(Desenvolvedor, '/hab/<int:id>')
api.add_resource(SelectandInclude,'/hab/')


if __name__ == "__main__":
    app.run(debug=True)