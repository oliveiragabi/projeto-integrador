# main.py

from flask import Blueprint, render_template, request,redirect,url_for,flash
from flask_login import login_required, current_user
import sqlite3 as sql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='template')

    app.config['SECRET_KEY'] = 'projeto.integrador.engenharia'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route("/add_user", methods=["POST","GET"])
def add_user(): # aqui a informação enviada do formulário pelo método POST é associado a cada variável, de cada campo da tabela
    if request.method == "POST":
       servico=request.form["servico"]
       dentrada=request.form["dentrada"]
       dsaida=request.form["dsaida"]
       descricao=request.form["descricao"]
       equipamento=request.form["equipamento"]
       nome=request.form["nome"]
       endereco=request.form["endereco"]
       fone=request.form["fone"]
       orcamento=request.form["orcamento"]

       con=sql.connect("db.sqlite") # começa a conexão co o banco de dados
       cur=con.cursor()
       cur.execute("insert into client(SERVICO,DENTRADA,DSAIDA,DESCRICAO,EQUIPAMENTO,NOME,ENDERECO,FONE,ORCAMENTO) values(?,?,?,?,?,?,?,?,?)",(servico,dentrada,dsaida,descricao,equipamento,nome,endereco,fone,orcamento))
       # esta sequência de interrogações serve para evitar sql injection
       con.commit()
       flash("Dados cadastrados","success") # mensagem para usuário, "success" será usado pelo bootstrap
       return redirect(url_for("login")) # terminado cadastro volta para a página inicial
    return render_template("add_user.html")

@main.route("/home", methods=["GET"])
def home():
    con = sql.connect("db.sqlite")
    con.row_factory=sql.Row # vai percorre as linhas do BD
    cur=con.cursor()
    cur.execute("select * from client")
    data=cur.fetchall() # variável data recebe todo conteúdo da tabela
    return render_template("home.html", datas=data) # datas vai receber conteudo da var data       

@main.route('/edit_user/<string:id>', methods=["POST","GET"]) # reconhecerá o usuário quando passar o id
def edit_user(id):
    if request.method=="POST":
       servico=request.form["servico"]
       dentrada=request.form["dentrada"]
       dsaida=request.form["dsaida"]
       descricao=request.form['descricao']
       equipamento=request.form["equipamento"]
       nome=request.form["nome"]
       endereco=request.form["endereco"]
       fone=request.form["fone"]
       orcamento=request.form["orcamento"]

       con=sql.connect("db.sqlite")
       cur=con.cursor()
       cur.execute("update client set SERVICO=?,DENTRADA=?,DSAIDA=?,DESCRICAO=?,EQUIPAMENTO=?,NOME=?,ENDERECO=?,FONE=? ,ORCAMENTO=? where ID=?",(servico,dentrada,dsaida,descricao,equipamento,nome,endereco,fone,orcamento,id))
       con.commit()
       flash("Dados atualizados", "success")
       return redirect(url_for("home")) # atualizou, volta para página inicial
    
    con=sql.connect("db.sqlite")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from client where ID=?",(id,))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@main.route("/delete_user/<string:id>", methods=["GET"])
def delete_user(id):
    con=sql.connect("db.sqlite")
    cur=con.cursor()
    cur.execute("delete from client where ID=?",(id,))
    con.commit()
    flash("Dados apagados", "warning")
    return redirect(url_for("home"))
