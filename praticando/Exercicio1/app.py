from flask import Flask,jsonify,request
app = Flask(__name__)

db = [{
        'id': 0,
        'Tarefas': ['Monitorar Turmas'],
        'Cargo': 'Monitor',
        'nome': 'Jose',
        'status': 'Pendente'},
        {
        'id': 1,
        'Tarefas': ['Corrigir Provas'],
        'Cargo':'Monitor',
        'nome': 'Pedro',
        'status': 'Pendente'
        }]

@app.route('/tarefa/<int:id>', methods = ['GET', 'POST','DELETE'])
def tarefas(id):
    if request.method == 'GET':
        try:
            response = db[id]
            return jsonify(response)
        except IndexError:
            return jsonify({'status': 'Not Found', 'msg': 'Usuario não encontrado.'})

    elif request.method == 'POST':
        db[id]['status'] = "feito"
        return jsonify(db[id])
    
    else:
        db.pop(id)
        return jsonify({'status': 'Sucesso', 'msg': 'Funcionario Excluido!'})

@app.route('/tarefa/' ,methods = ['GET'])
def Selectall():
        return jsonify(db)

          
if __name__ == "__main__":
    app.run(debug = True)