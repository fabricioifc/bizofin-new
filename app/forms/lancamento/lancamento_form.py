from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, DateField, BooleanField, SubmitField, FloatField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from flask_login import current_user
from app.models import User, Lancamento, Conta

def get_contas():
    return [(g.id, g.nome) for g in Conta.query.filter_by(user_id=current_user.id).order_by('nome')]

class LancamentoForm(FlaskForm):
    despesa = RadioField('Despesa', 
                         choices=[(1,'Despesa'),(0,'Receita')], 
                         default=1, 
                         coerce=bool, 
                         validate_choice=True, 
                         validators=[DataRequired()],
                         render_kw={
                            'form_type': 'inline'
                         },
    )
    descricao = StringField(label=('Descrição'),
                     validators=[DataRequired(), Length(3, 140)],
                     render_kw={
                       'autofocus': True,
                       'placeholder': 'Descrição'
                     })
    dtlancamento = DateField(
        "Dtlancamento", 
        default=datetime.now(),
        validators=[DataRequired()]
    )
    conta_id = SelectField(label=('Selecione a Conta'), 
                           choices=get_contas,
                           validators=[DataRequired()]
    )
    valor = FloatField(label=('Valor'),
                    validators=[DataRequired()],
                    render_kw={
                    'placeholder': 'Valor'
                    })
    # ativo = BooleanField('Ativo', default="checked")
    submit = SubmitField(label=('Salvar'))


    # def validate(self, extra_validators=None):
    #     initial_validation = super(LancamentoForm, self).validate(extra_validators)
    #     if not initial_validation:
    #         return False
    #     user = User.query.filter_by(email=self.email.data).first()
    #     if user:
    #         self.email.errors.append("Email already registered")
    #         return False
    #     if self.password.data != self.confirm.data:
    #         self.password.errors.append("Passwords must match")
    #         return False
    #     return True