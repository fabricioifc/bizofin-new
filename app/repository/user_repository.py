from app.models.user import User
from flask_login import LoginManager
from app.models.user import User
from flask_bcrypt import check_password_hash
from app.extensions import db

def get_user_by_id(user_id):
    return User.query.filter(User.id == int(user_id)).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def fazer_login(form):
    user = get_user_by_email(form.email.data)
    if user:
        if check_password_hash(user.password, form.password.data):
            return user
    
def registrar_usuario(form):
  user = User(email=form.email.data, password=form.password.data)
  db.session.add(user)
  db.session.commit()
  return user