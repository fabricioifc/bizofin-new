from app.models.task import Task
from app.extensions import db

def get_tasks(user_id):
  return Task.query.filter_by(user_id=user_id).all()

def get_task_by_id(user_id, task_id):
    return Task.query.filter_by(user_id=user_id, id=task_id).first()

def salvar_task(task: Task):
    db.session.add(task)
    db.session.commit()

def atualizar_task(task: Task):
    try:
        db.session.commit()
    except:
        db.session.rollback()

def deletar_task(task):
    try:
        db.session.delete(task)
        db.session.commit()
    except:
        db.session.rollback()