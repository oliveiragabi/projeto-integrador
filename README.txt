Para conseguir rodar o projeto, rode os seguintes comandos dentro da pasta projeto-integrador (estou uando o terminal do Vscode): 
- virtualenv env ou python -m venv env
Após a criação da pasta env, va na aba de pesquisa do seu pc e digite cmd, selecione a opção para executar como administrador 
- caminhe até a pasta .\env\Scripts\, ao chegar rode apenas o comando activate (sem cd e nem nada, vc nao vai entrar em uma pasta, mas sim rodar um arquivo)
Volte no vscode, feche o terminal cmd que estava usando, abra outro e rode dentro da pasta /src:
- pip install Flask Flask-Login Flask-Bcrypt Flask-WTF FLask-Migrate Flask-SQLAlchemy Flask-Testing python-decouple werkzeug jinja2
Após isso, rode:
-  set FLASK_APP=__init__.py e rode flask run
