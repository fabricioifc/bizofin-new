from app.models.lancamento import Lancamento
from app.extensions import db

def get_lancamentos(user_id):
  return Lancamento.query.filter_by(user_id=user_id, ativo=True).order_by('dtlancamento')

def salvar_lancamento(lancamento: Lancamento):
    db.session.add(lancamento)
    db.session.commit()

def atualizar_lancamento(lancamento: Lancamento):
    try:
        db.session.commit()
    except:
        db.session.rollback()

def deletar_lancamento(lancamento):
    try:
        db.session.commit()
    except:
        db.session.rollback()