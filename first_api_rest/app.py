from flask import Flask,jsonify,request
import json

#Conceituando uma API REST 
app = Flask(__name__)

desenvolvedores = [{
                    'id': 0,
                    'Nome': 'Jose Antonio',
                    'Habilidade': ['Python', 'Flask', 'MySQL', 'SQLAlchemy']},
                    

                    {
                    'id': 1,
                    'Nome': 'Kirk Jhonson',
                    'Habilidade': ['Html', 'CSS', 'JavaScript', 'NodJs']
                    }]

@app.route('/dev/<int:id>', methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
#metodo GET para pegar o usuario indentificado pelo parametro id
    if request.method == 'GET': 
        try:
            response = desenvolvedores[id]

        except IndexError:
            msg = (f'Desenvolvedor de ID {id} não existe.')
            response = {'status': 'Erro 404', 'menssagem': msg}
        except Exception:
            msg = 'Erro desconhecido, entre em contato com o adm da API'
            response = {'status': 'Erro', 'menssagem': msg}

        return jsonify(response)
#metodo para alterar usando um paramentro "dados" tratado para json ja que nosso date conceitual esta neste formato
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
#metodo DELETE usando a função POP e passando o id do usuario como parametro
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso', 'menssagem': 'Registro excluido'})

@app.route('/dev/', methods = ['POST','GET'])
def selectall():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao 
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    else:
        return jsonify(desenvolvedores)
        
if __name__ == "__main__":
    app.run(debug=True)