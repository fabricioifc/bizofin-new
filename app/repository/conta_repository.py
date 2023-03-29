from app.models.conta import Conta
from app.extensions import db

def get_contas(user_id):
    # contas = Conta.query.all()
  return Conta.query.filter_by(user_id=user_id).all()

def salvar_conta(conta: Conta):
    db.session.add(conta)
    db.session.commit()

def atualizar_conta(conta: Conta):
    try:
        db.session.commit()
    except:
        db.session.rollback()

def deletar_conta(conta):
    try:
        db.session.delete(conta)
        db.session.commit()
    except:
        db.session.rollback()