from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from ..extensions import db
from app.models.task import Task
from app.forms.task.task_form import TasksForm

from flask_breadcrumbs import register_breadcrumb
from flask_login import login_required, current_user
from app.repository.task_repository import *

bp_tarefas = Blueprint('tarefas', __name__, template_folder='templates', url_prefix='/tarefas')

@bp_tarefas.route('/')
@register_breadcrumb(bp_tarefas, '.', 'Tarefas')
@login_required
def index():
  tasks = get_tasks(current_user.id)
  return render_template('tarefas/index.html', lista=tasks)

@bp_tarefas.route('/create', methods=['GET', 'POST'])
@register_breadcrumb(bp_tarefas, '.create', 'Nova Tarefa')
@login_required
def create():
  form = TasksForm(ativo=True)
  if request.method == 'GET':
    return render_template('tarefas/create.html', form=form)
  else:
    if form.validate_on_submit():
      nome = request.form.get('name')
      ativo = bool(request.form.get('done'))

      objeto = Task(nome, current_user.id, ativo)
      salvar_task(objeto)

      flash('Tarefa Cadastrada com Sucesso!', "success")
      return redirect(url_for('tarefas.index'))
    else:
      return render_template('tarefas.create', form=form)


@bp_tarefas.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  objeto = Task.query.get_or_404(id)
  form = TasksForm(obj=objeto)
  if request.method == 'POST':
    objeto.name = request.form.get('name')
    objeto.done = bool(request.form.get('done'))
    try:
      atualizar_task(objeto)
      flash("Tarefa Atualizada com Sucesso!", "success")
      return redirect(url_for('tarefas.index'))
    except:
      flash("Ocorreu um erro inesperado!", "danger")
      return render_template('tarefas/update.html', form=form)

  return render_template('tarefas/update.html', form=form)


@bp_tarefas.route('/delete/<int:id>', methods=['GET','POST', 'DELETE'])
@login_required
def delete(id):
  objeto = get_task_by_id(current_user.id, id)
  if objeto is None:
    abort(404)
    
  if request.method in ['DELETE', 'POST']:
    try:
      deletar_task(objeto)
      flash("Tarefa Removida com Sucesso!", "success")
      return redirect(url_for('tarefas.index'))
    except:
      flash("Ocorreu um erro inesperado!", "danger")
      return render_template('tarefas/index.html')
  else:
    return render_template('tarefas/delete.html', objeto=objeto)