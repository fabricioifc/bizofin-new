import os
from datetime import datetime
from flask_login import UserMixin
from ..extensions import db, bcrypt

from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from dotenv import load_dotenv

load_dotenv('.flaskenv')

class User(UserMixin, db.Model):

  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  created_on = db.Column(db.DateTime, nullable=False)
  is_admin = db.Column(db.Boolean, nullable=False, default=False)

  def __init__(self, email, password, is_admin=False):
    self.email = email
    self.password = bcrypt.generate_password_hash(password)
    self.created_on = datetime.now()
    self.is_admin = is_admin

  def __repr__(self):
    return f"<email {self.email}>"

  def get_token(self):
    serial = Serializer(os.getenv('SECRET_KEY'))
    return serial.dumps({'user_id': self.id})
  
  @staticmethod
  def verify_token(token):
    serial = Serializer(os.getenv('SECRET_KEY'))
    try:
      user_id = serial.loads(token)['user_id']
    except:
      return None
    
    return User.query.get(user_id)