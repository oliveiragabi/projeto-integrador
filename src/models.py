from flask_login import UserMixin
from . import db

class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary keys
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    servico = db.Column(db.String(100))
    dentrada = db.Column(db.String(50))
    dsaida = db.Column(db.String(50))
    descricao = db.Column(db.String(200))
    equipamento = db.Column(db.String(100))
    nome = db.Column(db.String(150))
    endereco = db.Column(db.String(200))
    fone = db.Column(db.String(200) )
    orcamento = db.Column(db.String(60))
    
class Aluguel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(100))
    dentrada = db.Column(db.String(50))
    dsaida = db.Column(db.String(50))
    descricao = db.Column(db.String(200))
    titulo = db.Column(db.String(100))
    nome = db.Column(db.String(150))
    cep = db.Column(db.String(200))
    rua = db.Column(db.String(200))
    numero = db.Column(db.String(200))
    fone = db.Column(db.String(200) )
    orcamento = db.Column(db.String(60))

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    autor = db.Column(db.String(100))
    editora = db.Column(db.String(50))
    data_lancamento = db.Column(db.String(200))
    descricao = db.Column(db.String(100))
    isbn = db.Column(db.String(150))

    