# import datetime
# from app.extensions import db

# class Task(db.Model):
#   """Task model."""
#   __tablename__ = 'tasks'

#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(45), nullable=False)
#   done = db.Column(db.Boolean(), default=False)
#   created_at = db.Column(db.DateTime, default=datetime.datetime.now)
#   updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#   user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

#   def __init__(self, name, user_id, done=False):
#     self.name = name
#     self.user_id = user_id
#     self.done = done

#   def __repr__(self):
#     return '<Task %r>' % self.name
  
#   def serialize(self):
#     return {
#       'id': self.id,
#       'name': self.name,
#       'done': self.done,
#       'created_at': self.created_at,
#       'updated_at': self.updated_at,
#       'user_id': self.user_id
#     }
  
#   def save(self):
#     db.session.add(self)
#     db.session.commit()

#   def delete(self):
#     db.session.delete(self)
#     db.session.commit()

#   def update(self, data):
#     for key, item in data.items():
#       setattr(self, key, item)
#     self.save()

# # Path: app\models\user.py
# import datetime
# from app.extensions import db

# class User(db.Model):
#   """User model."""
#   __tablename__ = 'users'

#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(45), nullable=False)
#   email = db.Column(db.String(45), nullable=False)
#   password = db.Column(db.String(255), nullable=False)
#   created_at = db.Column(db.DateTime, default=datetime.datetime.now)
#   updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
#   tasks = db.relationship('Task', backref='user', lazy=True)

#   def __init__(self, username, email, password):
#     self.username = username
#     self.email = email
#     self.password = password

#   def __repr__(self):
#     return '<User %r>' % self.username
  
#   def serialize(self):
#     return {
#       'id': self.id,
#       'username': self.username,
#       'email': self.email,
#       'password': self.password,
#       'created_at': self.created_at,
#       'updated_at': self.updated_at,
#       'tasks': [task.serialize() for task in self.tasks]
#     }
  
#   def save(self):
#     db.session.add(self)
#     db.session.commit()

#   def delete(self):
#     db.session.delete(self)
#     db.session.commit()

#   def update(self, data):
#     for key, item in data.items():
#       setattr(self, key, item)
#     self.save()

# # Path: app\extensions.py
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_jwt_extended import JWTManager

# db = SQLAlchemy()
# migrate = Migrate()
# jwt = JWTManager()

# # Path: app\__init__.py
# from flask import Flask
# from flask_cors import CORS
# from app.extensions import db, migrate, jwt
# from app.config import Config
# from app.routes import api

# def create_app(config_class=Config):
#   app = Flask(__name__)
#   app.config.from_object(config_class)
#   CORS(app)

#   db.init_app(app)
#   migrate.init_app(app, db)
#   jwt.init_app(app)

#   app.register_blueprint(api)

#   return app
