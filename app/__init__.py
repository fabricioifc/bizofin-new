import os
from flask import Flask, session, abort, redirect, request

from dotenv import load_dotenv
load_dotenv('.flaskenv')

def create_app():
  app = Flask(__name__)
  
  registrar_configuracoes(app)
  registrar_extensoes(app)
  registrar_blueprints(app)
  registrar_handlers(app)
  registrar_email(app)

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
  from .extensions import db, migrate, bcrypt, bootstrap5, breadcrumbs, babel

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

  babel.init_app(app, default_locale='pt_br')

def registrar_configuracoes(app):
  # Configure the flask app instance
  CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
  app.config.from_object(CONFIG_TYPE)


def registrar_email(app):
  from .extensions import mail

  # app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
  # app.config['MAIL_PORT'] = 2525
  # app.config['MAIL_USERNAME'] = '1e7215eeae5c17'
  # app.config['MAIL_PASSWORD'] = '09d5bad3f597e4'
  # app.config['MAIL_USE_TLS'] = True
  # app.config['MAIL_USE_SSL'] = False
  app.config['MAIL_SERVER']='smtp.mailgun.org'
  app.config['MAIL_PORT'] = 587
  app.config['MAIL_USERNAME'] = 'postmaster@sandbox2fa2926b85d6487a974a644e3311d8aa.mailgun.org'
  app.config['MAIL_PASSWORD'] = 'ef09004e04fca16e08aacb5111eca261-d51642fa-b180737c'
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USE_SSL'] = False
  mail.init_app(app)

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
