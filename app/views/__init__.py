from .account import bp_account
from .contas import bp_contas
from .lancamentos import bp_lancamentos
from .home import bp_main
from .tasks import bp_tarefas

views = [bp_lancamentos, bp_account, bp_contas, bp_main, bp_tarefas]