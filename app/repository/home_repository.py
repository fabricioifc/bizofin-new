from app.models.lancamento import Lancamento
from app.models.conta import Conta
from app.extensions import db
from flask_login import current_user
from sqlalchemy.sql import text

'''Retorna as contas do usuário e seu respectivo saldo'''
def get_saldo_contas():
    stmt = (
        db.session.query(
            Lancamento.conta_id.label('conta_id'),
            db.func.sum(Lancamento.valor).label("saldo"),
        )
        .filter_by(user_id=current_user.id, ativo=True)
        .group_by(Lancamento.conta_id)
        .subquery()
    )

    result = (
        db.session.query(
            Conta.nome.label('nome'),
            stmt.c.conta_id.label('conta_id'),
            stmt.c.saldo.label('saldo'),
        )
        .filter_by(user_id=current_user.id, ativo=True)
        .join(stmt, Conta.id == stmt.c.conta_id, isouter=True)
        .order_by(Conta.id).all()
    )

    fields = ['conta', 'id', 'saldo', 'cor']
    result = [dict(zip(fields, d)) for d in result]

    return result