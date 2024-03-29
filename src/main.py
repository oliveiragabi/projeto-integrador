# main.py

from flask import Blueprint, render_template, request,redirect,url_for,flash
from flask_login import login_required, current_user
import sqlite3 as sql
from . import db
from .models import Client
from .models import Livro
from .models import Aluguel


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models

main = Blueprint('main', __name__, static_folder='static')

@main.route('/')
def index():
    return render_template('index.html')

@main.route("/add_user", methods=["POST","GET"])
def add_user(): # aqui a informação enviada do formulário pelo método POST é associado a cada variável, de cada campo da tabela
    if request.method == "POST":
       servico=request.form.get('servico')
       dentrada=request.form.get('dentrada')
       if(len(request.form.get('dsaida')) == 0):
           dsaida = "sem data"
       else:
           dsaida = request.form.get('dsaida')
       descricao=request.form.get('descricao')
       equipamento=request.form.get('equipamento')
       nome=request.form.get('nome')
       endereco=request.form.get('endereco')
       fone=request.form.get('fone')
       orcamento=request.form.get('orcamento')
           
       if(dentrada > dsaida):
         flash("A data de entrada nao deve ser maior que a data de saida")
  

       new_client = Client(servico=servico, dentrada=dentrada, dsaida=dsaida, descricao=descricao, 
                           equipamento=equipamento, nome=nome, endereco=endereco, fone=fone, orcamento=orcamento )
       
       db.session.add(new_client)
       db.session.commit()

       flash("Dados cadastrados","success") # mensagem para usuário, "success" será usado pelo bootstrap
       return redirect(url_for("main.home")) # terminado cadastro volta para a página inicial
    return render_template("add_user.html")

@main.route("/home", methods=["GET"])
def home():
    clients = Client.query.all()
    return render_template("home.html", clients=clients) # datas vai receber conteudo da var data       

@main.route('/edit_user/<string:id>', methods=["POST","GET"]) # reconhecerá o usuário quando passar o id
def edit_user(id):
    if request.method=="POST":
       update_cli = Client.query.get(id)
       update_cli.servico = request.form.get('servico')
       update_cli.dentrada=request.form.get('dentrada')
       update_cli.dsaida=request.form.get('dsaida')
       update_cli.descricao=request.form.get('descricao')
       update_cli.equipamento=request.form.get('equipamento')
       update_cli.nome=request.form.get('nome')
       update_cli.endereco=request.form.get('endereco')
       update_cli.fone=request.form.get('fone')
       update_cli.orcamento=request.form.get('orcamento')
       db.session.commit()
       flash("Dados atualizados", "success")
       return redirect(url_for("main.home")) # atualizou, volta para página inicial
    

    data = Client.query.filter_by(id=id).first()
    return render_template("edit_user.html", datas=data)


@main.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):

    update_cli = Client.query.get(id)
    db.session.delete(update_cli)

    db.session.commit()
    flash("Dados apagados", "warning")
    return redirect(url_for("main.home"))


@main.route("/add_livro", methods=["POST","GET"])
def add_livro(): # aqui a informação enviada do formulário pelo método POST é associado a cada variável, de cada campo da tabela
    if request.method == "POST":
       titulo=request.form.get('titulo')
       autor=request.form.get('autor')
       editora=request.form.get('descricao')
       data_lancamento=request.form.get('data_lancamento')
       descricao=request.form.get('descricao')
       isbn=request.form.get('isbn')
  
       novo_livro = Livro(titulo=titulo, autor=autor, editora=editora, data_lancamento=data_lancamento, descricao=descricao,
                           isbn=isbn)
       
       db.session.add(novo_livro)
       db.session.commit()

       flash("Dados cadastrados","success") # mensagem para usuário, "success" será usado pelo bootstrap
       return redirect(url_for("main.home")) # terminado cadastro volta para a página inicial
    return render_template("add_livro.html")

@main.route("/add_aluguel", methods=["POST","GET"])
def add_aluguel(): # aqui a informação enviada do formulário pelo método POST é associado a cada variável, de cada campo da tabela
    if request.method == "POST":
       isbn=request.form.get('isbn')
       dentrada=request.form.get('dentrada')
       if(len(request.form.get('dsaida')) == 0):
           dsaida = "sem data"
       else:
           dsaida = request.form.get('dsaida')
       descricao=request.form.get('descricao')
       titulo=request.form.get('data_lancamento')
       nome=request.form.get('isbn')
       cep=request.form.get('cep')
       rua=request.form.get('rua')
       numero=request.form.get('numero')
       fone=request.form.get('fone')
       orcamento=request.form.get('orcamento')
  

       novo_aluguel = Aluguel(isbn=isbn, dentrada=dentrada, dsaida=dsaida, descricao=descricao, 
                           titulo=titulo, nome=nome, cep=cep, rua=rua, numero=numero, fone=fone, orcamento=orcamento )
       
       db.session.add(novo_aluguel)
       db.session.commit()

       flash("Dados cadastrados","success") # mensagem para usuário, "success" será usado pelo bootstrap
       return redirect(url_for("main.home")) # terminado cadastro volta para a página inicial
    return render_template("add_aluguel.html")
