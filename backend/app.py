from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True, primary_key=True)
    email = db.Column(db.String(120),unique=True ,nullable=False)

    def __init__(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}
    
db.create_all()

@app.route('/users', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})