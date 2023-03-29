from datetime import datetime
from ..extensions import db

class Lancamento(db.Model):

  __tablename__ = 'lancamentos'

  id = db.Column(db.Integer, primary_key=True)
  descricao = db.Column(db.String(140), nullable=False)
  dtlancamento = db.Column(db.DateTime, nullable=False)
  valor = db.Column(db.Float, nullable=False)
  ativo = db.Column(db.Boolean(), default=True)

  conta_id = db.Column(db.Integer, db.ForeignKey('contas.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, descricao, dtlancamento, valor, conta_id, user_id, ativo=True):
    self.descricao = descricao
    self.dtlancamento = dtlancamento
    self.valor = valor
    self.conta_id = conta_id
    self.user_id = user_id
    self.ativo = ativo

  def __repr__(self, ):
    return 'Lancamento: {}{}{}'.format(self.descricao, self.valor, self.conta_id)
