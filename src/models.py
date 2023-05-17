from flask_login import UserMixin
from . import db

class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String(100), unique=True)
    dentrada = db.Column(db.Integer, primary_key=True)
    dsaida = db.Column(db.Date, primary_key=True)
    descricao = db.Column(db.String(200), unique=True)
    equipamento = db.Column(db.String(100), unique=True)
    nome = db.Column(db.String(150), unique=True)
    endereco = db.Column(db.String(200), unique=True)
    fone = db.Column(db.Integer, primary_key=True)
    orcamento = db.Column(db.Double, primary_key=True)
