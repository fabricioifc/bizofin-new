from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..extensions import db
from app.models.conta import Conta
from app.forms.conta.conta_form import ContasForm

from flask_breadcrumbs import register_breadcrumb, default_breadcrumb_root
from flask_login import login_required, current_user
from app.repository.conta_repository import *

bp_contas = Blueprint('contas', __name__, template_folder='templates', url_prefix='/contas')

@bp_contas.route('/')
@register_breadcrumb(bp_contas, '.', 'Contas')
@login_required
def index():
  contas = get_contas(current_user.id)
  return render_template('contas/index.html', contas=contas)

@bp_contas.route('/create', methods=['GET', 'POST'])
@register_breadcrumb(bp_contas, '.create', 'Nova Conta')
@login_required
def create():
  form = ContasForm(ativo=True)
  if request.method == 'GET':
    return render_template('contas/create.html', form=form)
  else:
    if form.validate_on_submit():
      nome = request.form.get('nome')
      ativo = bool(request.form.get('ativo'))

      conta = Conta(nome, current_user.id, ativo)
      salvar_conta(conta)

      flash('Conta Cadastrada com Sucesso!', "success")
      return redirect(url_for('contas.index'))
    else:
      return render_template('contas.create', form=form)


@bp_contas.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  conta = Conta.query.get_or_404(id)
  form = ContasForm(obj=conta)
  if request.method == 'POST':
    conta.nome = request.form.get('nome')
    conta.ativo = bool(request.form.get('ativo'))
    try:
      atualizar_conta(conta)
      flash("Conta Atualizada com Sucesso!", "success")
      return redirect(url_for('contas.index'))
    except:
      flash("Ocorreu um erro inesperado!", "danger")
      return render_template('contas/update.html', form=form)

  return render_template('contas/update.html', form=form)


@bp_contas.route('/delete/<int:id>', methods=['GET', 'POST', 'DELETE'])
@login_required
def delete(id):
  conta = Conta.query.get_or_404(id)
  if request.method in ['DELETE', 'POST']:
    try:
      deletar_conta(conta)
      flash("Conta Removida com Sucesso!", "success")
      return redirect(url_for('contas.index'))
    except:
      flash("Ocorreu um erro inesperado!", "danger")
      return render_template('contas/index.html')
  else:
    return render_template('contas/delete.html', conta=conta)