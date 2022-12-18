from flask import Flask, jsonify, request
import json
#"jsonify" permite receber informação em formato json
app = Flask(__name__)

@app.route('/<int:id>')
def creater_api(id):
    return jsonify({
        'id': id,
        'name': 'Jose Antonio',
        'profissao': 'Programador'
    })

@app.route('/soma', methods = ['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados["Valores"])
    print(dados)
    return jsonify(total)
    
    
if __name__ == "__main__":
    app.run(debug=True)