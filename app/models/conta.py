# from datetime import datetime
from ..extensions import db

class Conta(db.Model):

  __tablename__ = 'contas'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(45), nullable=False)
  ativo = db.Column(db.Boolean(), default=True)
  
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  # lancamentos = db.relationship("Lancamento", foreign_keys='Lancamento.conta_id', lazy='joined', innerjoin=True)
  lancamentos = db.relationship("Lancamento", 
                                lazy='joined',
                                backref='conta',
                                cascade="all, delete-orphan",)


  def __init__(self, nome, user_id, ativo=True):
    self.nome = nome
    self.user_id = user_id
    self.ativo = ativo

  # def saldo(self):
  #   # saldo = [sum(x[0].valor) for x in zip(self.lancamentos)]

  #   saldo = 0.0
  #   for x in zip(self.lancamentos):
  #     saldo += x[0].valor
  #   return saldo

  def __repr__(self, ):
    return '{}-{}'.format(self.id, self.nome)
