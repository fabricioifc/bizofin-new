import datetime
from app.extensions import db

class Task(db.Model):
  """Task model."""
  __tablename__ = 'tasks'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(140), nullable=False)
  done = db.Column(db.Boolean(), default=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, name, user_id, done=False):
    self.name = name
    self.user_id = user_id
    self.done = done

  def __repr__(self):
    return '<Task %r>' % self.name
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'done': self.done,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'user_id': self.user_id
    }
  