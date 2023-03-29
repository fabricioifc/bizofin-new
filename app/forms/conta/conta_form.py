from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *

class ContasForm(FlaskForm):
  nome = StringField(label=('Nome da Conta'),
                     validators=[DataRequired(), Length(2, 45)],
                     render_kw={
                       'autofocus': True,
                       'placeholder': 'Nome da Conta'
                     })
  ativo = BooleanField('Ativo', default="checked")
  submit = SubmitField(label=('Salvar'))
