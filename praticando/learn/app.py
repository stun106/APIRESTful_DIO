from flask import Flask,request,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


#"sqlite:/// app.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/app_db"
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)




class Database(db.Model):
    __tablename__ = "devs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True, index = True)
    skil = db.Column(db.String(50))
    
    def serialize(self):
        return {
        "id": self.id,
        "name": self.name,
        "username": self.username,
        "password": self.password,
        "email": self.email,
        "skill": self.skil
            }

class dev(Resource):
    def get(self,id):
        Query = Database.query.filter_by(id=id).first_or_404()
        return jsonify(Query.serialize())
    
    def put(self,id):
        dados = request.get_json()
        Query = Database.query.filter_by(id=id).first()
        Query.name = dados["name"]
        Query.username = dados["username"]
        Query.email = dados['email']
        Query.skil = dados["skill"]
        db.session.commit()
        return jsonify({"Menssagem":"Dados Alterados com sucesso!"})
    
    def delete(self,id):
        Query = Database.query.filter_by(id=id).first()
        db.session.delete(Query)
        db.session.commit()
        return jsonify({"menssagem":"usuario Excluido."})
    
class AddandList(Resource):
    def post(self):
        dados = request.get_json()
        new_user = Database(
                            skil=dados['skill'],
                            name=dados['name'],
                            username=dados['username'],
                            password=dados['password'],
                            email=dados['email']
                            )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"Menssagem":"Dados Cadastrados com sucesso!"})
    def get(self):
        Query = Database.query.all()
        serialized_devs = [devs.serialize() for devs in Query]
        return jsonify(serialized_devs)
    
        
    

    
with app.app_context():
    db.create_all()

api.add_resource(dev,"/dev/<int:id>")
api.add_resource(AddandList,"/dev/")


if __name__ == '__main__':
    app.run(debug=True)