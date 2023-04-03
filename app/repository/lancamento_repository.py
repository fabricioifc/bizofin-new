import datetime, calendar
from app.models.lancamento import Lancamento
from app.repository.conta_repository import get_contas
from app.extensions import db
from sqlalchemy import func
from app.models.conta import Conta

# def get_lancamentos(user_id):
#   return Lancamento.query.filter_by(user_id=user_id, ativo=True).order_by('dtlancamento')

# def get_lancamentos_conta(user_id, conta_id):
#   return Lancamento.query.filter_by(user_id=user_id, ativo=True, conta_id=conta_id).order_by('dtlancamento')

def get_lancamentos_by_id(user_id, lancamento_id):
    return Lancamento.query.filter_by(user_id=user_id, id=lancamento_id).first()

def get_lancamentos_anomes(user_id, ano, mes, conta_id=None):
    dias = calendar.monthrange(ano, mes)
    dtini = datetime.datetime(year=ano, month=mes, day=1).strftime('%Y-%m-%d')  
    dtfim = datetime.datetime(year=ano, month=mes, day=dias[1]).strftime('%Y-%m-%d')

    lancamentos = Lancamento.query.filter(
        Lancamento.user_id==user_id, Lancamento.ativo==True, (conta_id is None or Lancamento.conta_id==conta_id),
        func.date(Lancamento.dtlancamento).between(dtini,dtfim)
    ).order_by('dtlancamento').all()

    saldo_anterior = get_saldo_contas(user_id=user_id, dtini=dtini, conta_id=conta_id)

    return lancamentos, saldo_anterior


'''Retorna as contas do usuário e seu respectivo saldo'''
def get_saldo_contas(user_id, dtini, conta_id) -> dict:
    
    query = (
        db.session.query(
            db.func.sum(Lancamento.valor).label("saldo"),
        )
        .filter(
            Lancamento.user_id==user_id, 
            Lancamento.ativo==True, 
            (conta_id is None or Lancamento.conta_id==conta_id),
            func.date(Lancamento.dtlancamento) < dtini
        ).first()
    )

    fields = ['saldo_inicial']
    # result = [dict(zip(fields, d)) for d in query]
    return dict(zip(fields, query))

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