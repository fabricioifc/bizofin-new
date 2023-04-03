from datetime import datetime as D
from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from ..extensions import db
from app.models import Conta, Lancamento
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *
from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required, current_user
from app.forms.lancamento.lancamento_form import LancamentoForm
from app.repository.lancamento_repository import *

bp_lancamentos = Blueprint('lancamentos', __name__, template_folder='templates', url_prefix='/lancamentos')

@bp_lancamentos.route('/')
# @bp_lancamentos.route('/<int:conta_id>/conta')
@bp_lancamentos.route('/<int:ano>/<int:mes>')
@bp_lancamentos.route('/<int:ano>/<int:mes>/conta/<int:conta_id>')
@register_breadcrumb(bp_lancamentos, '.', 'Lançamentos')
@login_required
def index(ano=None, mes=None, conta_id=None):

  if ano is None or mes is None:
    return redirect(url_for('lancamentos.index', ano=datetime.datetime.now().year, mes=datetime.datetime.now().month))

  (lancamentos_anomes, saldo_anterior) = get_lancamentos_anomes(user_id=current_user.id,ano=ano,mes=mes,conta_id=conta_id)
  contas = get_contas(user_id=current_user.id)

  return render_template('lancamentos/index.html', 
                          lancamentos=lancamentos_anomes, 
                          contas=contas, saldo_anterior=saldo_anterior['saldo_inicial'] or 0,
                          ano_atual=ano, mes_atual=mes, conta_atual=conta_id)


@bp_lancamentos.route('/create', methods=['GET', 'POST'])
@register_breadcrumb(bp_lancamentos, '.create', 'Novo Lançamento')
@login_required
def create():
  form = LancamentoForm(ativo=True)
  if request.method == 'GET':
    return render_template('lancamentos/create.html', form=form)
  else:
    if form.validate_on_submit():
      descricao = request.form.get('descricao')
      dtlancamento = request.form.get('dtlancamento')
      conta_id = request.form.get('conta_id')
      # ativo = bool(request.form.get('ativo'))
      despesa = bool(int(request.form.get('despesa')))
      valor = round(float(request.form.get('valor')), 2)

      lancamento = Lancamento(
        ativo=True,
        conta_id=conta_id,
        descricao=descricao,
        dtlancamento=D.strptime(dtlancamento, '%Y-%m-%d'),
        user_id=current_user.id,
        valor=valor*-1 if despesa else valor
      )

      salvar_lancamento(lancamento)

      flash('Lançamento Cadastrado com Sucesso!', "success")
      return redirect(url_for('lancamentos.index'))
    else:
      return render_template('lancamentos/create.html', form=form)


@bp_lancamentos.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  lancamento = get_lancamentos_by_id(current_user.id, id)
  if lancamento is None:
    abort(404)

  form = LancamentoForm(obj=lancamento)
  if form.validate_on_submit():
    try:
      form.populate_obj(lancamento)
      despesa = bool(int(request.form.get('despesa')))
      valor = round(float(request.form.get('valor')), 2)
      lancamento.valor = valor*-1 if despesa else valor

      atualizar_lancamento(lancamento=lancamento)
      flash("Lançamento Atualizado com Sucesso!", "success")
      return redirect(url_for('lancamentos.index'))
    except Exception as e:
      flash(e, "danger")
      return render_template('lancamentos/update.html', form=form)
  else:
    # Definindo o valor do RadioField para a tela
    despesa=lancamento.valor < 0
    # Normalizando o valor para não ficar menor que zero na tela
    lancamento.valor = lancamento.valor * -1 if lancamento.valor < 0 else lancamento.valor
    form = LancamentoForm(obj=lancamento, despesa=despesa)
    return render_template('lancamentos/update.html', form=form)


@bp_lancamentos.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
  # lancamento = Lancamento.query.get_or_404(id)
  lancamento = get_lancamentos_by_id(current_user.id, id)
  if lancamento is None:
    abort(404)
    
  if request.method in ['POST']:
    try:
      lancamento.ativo = False
      deletar_lancamento(lancamento=lancamento)

      flash("Lançamento Removido com Sucesso!", "success")
      return redirect(url_for('lancamentos.index'))
    except:
      flash("Ocorreu um erro inesperado!", "danger")
      return render_template('lancamentos/index.html')
  else:
    return render_template('lancamentos/delete.html', lancamento=lancamento)
  

# def get_contas():      
#     return Conta.query.filter_by(user_id=current_user.id).all()