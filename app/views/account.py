from flask import Blueprint, render_template, request, flash, redirect, url_for, session, abort
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from app.models.user import User
from app.forms.login_form import LoginForm, ResetForm, ChangePasswordForm, ResetPasswordForm
from app.forms.register_form import RegisterForm
from ..extensions import db, bcrypt, mail

from app.repository.user_repository import fazer_login, registrar_usuario, get_user_by_id

bp_account = Blueprint('accounts', __name__, template_folder='templates', url_prefix='/accounts')

def redirect_dest(home='main.index'):
  dest_url = request.args.get('next')
  if not dest_url:
    dest_url = url_for(home)
  return redirect(dest_url)

@bp_account.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    flash('Você já está logado.', "info")
    return redirect(url_for('main.index'))

  form = LoginForm(request.form)
  if form.validate_on_submit():
    try:
      user = fazer_login(form)
      if user:
        login_user(user)
        return redirect_dest()
      else:
        flash("Nome de usuário ou senha inválidos!", "danger")
        return render_template("accounts/login.html", form=form)
    except Exception as e:
      flash(e, "danger")

  return render_template("accounts/login.html", form=form)

@bp_account.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    flash("Você já está registrado.", "info")
    return redirect(url_for("main.index"))
  
  form = RegisterForm(request.form)
  if form.validate_on_submit():
    user = registrar_usuario(form)

    if user:
      login_user(user)
      flash("Você se registrou e agora está logado. Bem-vindo!", "success")
      return redirect(url_for("main.index"))

  return render_template("accounts/register.html", form=form)

@bp_account.route("/logout")
@login_required
def logout():
  logout_user()
  flash("Você foi desconectado.", "success")
  return redirect(url_for("accounts.login"))

@bp_account.route("/reset_password", methods=['GET', 'POST'])
def reset():
  form = ResetForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      send_mail(user)
    flash('Uma mensagem foi enviada para o seu e-mail. Verifique.', 'success')
    return redirect(url_for('accounts.login'))
  return render_template("accounts/reset.html", form=form)

def send_mail(user: User):
  from flask_mail import Message
  token = user.get_token()
  message = Message('Recuperação de Senha', recipients=[user.email], sender='fabricio.bizotto@gmail.com')
  message.body=f'''
    Para reiniciar sua senha, clique no link abaixo.
    {url_for('accounts.reset_token', token=token, _external=True)}
  '''

  mail.send(message)

@bp_account.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
  user = User.verify_token(token)
  if user is None:
    flash('Token Inválido ou Expirou!')
    return redirect(url_for('accounts.reset'))
  
  form = ResetPasswordForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
    user.password=hashed_password
    print(hashed_password)
    db.session.commit()
    flash('Senha alterada com sucesso!', 'success')
    return redirect(url_for('accounts.login'))
  return render_template('accounts/change.html', form=form)

# Gerenciador de Login
def setup_flask_login(app):
  from flask_login import LoginManager
  
  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = "accounts.login"
  login_manager.login_message = 'Por favor, faça o login para acessar esta página.'
  login_manager.login_message_category = 'warning'

  # Callback para recarregar o usuário armazenado na sessão
  @login_manager.user_loader
  def load_user(user_id):
    return get_user_by_id(user_id=user_id)