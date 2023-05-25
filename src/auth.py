# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import Employee
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Employee.query.filter_by(email=email).first()

    # checa se o usuario existe
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # se o usuario n existir ou a senha estiver errada, recarrega a mesma pagina

    # se a checagem passar, leva o usuario para a home (onde tem a lista de serviço)
    login_user(user, remember=remember)
    return redirect(url_for('main.home'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = Employee.query.filter_by(email=email).first() # filtra usuario por email

    if user: # se o email existir, exibe a msg e retorna a pagina de signup  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # cria um novo usuario com os dados do form. transforma a senha em hash code.
    new_user = Employee(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # adc o usuario banco de dados
    db.session.add(new_user)
    db.session.commit()
    

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))