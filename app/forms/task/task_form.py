from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms.fields import *

class TasksForm(FlaskForm):
  name = StringField(label=('Descrição da Tarefa'),
                     validators=[DataRequired(), Length(1, 144)],
                     render_kw={
                       'autofocus': True,
                       'placeholder': 'Tarefa'
                     })
  done = BooleanField('Feira', default="checked")
  submit = SubmitField(label=('Salvar'))
