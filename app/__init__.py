import os
from flask import Flask, session, abort, redirect, request

# from dotenv import load_dotenv
# load_dotenv('.flaskenv')

def create_app():
  app = Flask(__name__)
  
  registrar_configuracoes(app)
  registrar_extensoes(app)
  registrar_blueprints(app)
  registrar_handlers(app)

  from app.views.account import setup_flask_login
  setup_flask_login(app)

  return app


### Helper Functions ###
def registrar_blueprints(app):
  from app.views import views

  # # Registrar as rotas
  # app.register_blueprint(bp_lancamentos, url_prefix='/lancamentos')
  # app.register_blueprint(bp_contas, url_prefix='/contas')
  # app.register_blueprint(bp_account, url_prefix='/accounts')
  # app.register_blueprint(bp_main)

  for view in views:
    app.register_blueprint(view)


def registrar_extensoes(app):
  from .extensions import db, migrate, bcrypt, bootstrap5, breadcrumbs

  # Inicializa o Banco de Dados SQLite
  db.init_app(app)

  # Executa as migrações das tabelas
  # Precisa executar `flask db init` `flask db migrate` no shell
  migrate.init_app(app, db)

  # Bootstrap (CSS)
  bootstrap5.init_app(app)

  # Breadcrumbs
  breadcrumbs.init_app(app=app)

  #Crypt password
  bcrypt.init_app(app)

  with app.app_context():
    db.create_all()

def registrar_configuracoes(app):
  # Configure the flask app instance
  CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
  app.config.from_object(CONFIG_TYPE)


def registrar_handlers(app):
  from flask import render_template

  @app.errorhandler(403)
  def forbidden(e):
      return render_template('error/403.html'), 403
  
  @app.errorhandler(404)
  def page_not_found(error):
    return render_template("error/404.html"), 404

  @app.errorhandler(500)
  def server_error(e):
      return render_template('error/500.html'), 500

  


# @app.route('/')
# @app.route('/home')
# @register_breadcrumb(app, '.', 'Início')
# def index():
#   return render_template('index.html')
#   # return redirect(url_for('/contas'))
