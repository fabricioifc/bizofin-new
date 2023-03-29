from flask import render_template, request, redirect, url_for
from flask import Blueprint
from flask_breadcrumbs import register_breadcrumb, default_breadcrumb_root
from flask_login import current_user
from sqlalchemy.sql import func
from app.repository.home_repository import get_saldo_contas

bp_main = Blueprint('main', __name__, template_folder='templates', url_prefix='/')
default_breadcrumb_root(bp_main, '.')

@bp_main.route('/')
@bp_main.route('/home')
@register_breadcrumb(bp_main, '.', 'Início')
# @default_breadcrumb_root(main_blueprint, '.')
def index():
    if current_user.is_authenticated:
        # Busca as contas com seu saldo
        conta_saldo = get_saldo_contas()
        # Adiciona a cor verde, caso o saldo seja positivo e vermelho caso seja negativo
        conta_saldo = [{**item, 'color': 'bg-success' if item['saldo'] > 0 else 'bg-danger'} for item in conta_saldo]

        return render_template('main/dashboard.html', saldo=conta_saldo)
    else:
        return render_template('main/index.html')
