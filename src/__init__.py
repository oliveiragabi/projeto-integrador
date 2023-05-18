# template_folder='template')
# init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# iniciando o SQLAlchemypara usar nos models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='template')

    app.config['SECRET_KEY'] = 'projeto.integrador.engenharia'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import Employee

    @login_manager.user_loader
    def load_user(user_id):
        # pega o funcionario pelo id
        return Employee.query.get(int(user_id))

    # blueprint para rota de autenticação do app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint para as rotas que nao necessitam de autenticação
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app