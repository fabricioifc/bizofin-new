from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo

class LoginForm(FlaskForm):
  email = EmailField("E-mail", validators=[DataRequired(), Email(message=None)], render_kw={'autofocus': True, })
  password = PasswordField("Senha", validators=[DataRequired()])

class ResetForm(FlaskForm):
  email = EmailField("E-mail", validators=[DataRequired(), Email(message=None)])
  submit = SubmitField(label=('Enviar e-mail de recuperação'))

class ResetPasswordForm(FlaskForm):
  password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
  )
  confirm = PasswordField(
    "Repeat password",
    validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match."),
    ],
  )
  submit = SubmitField(label=('Alterar Senha'))

class ChangePasswordForm(FlaskForm):
  email = EmailField("E-mail", validators=[DataRequired(), Email(message=None)])
  password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
  )
  confirm = PasswordField(
    "Repeat password",
    validators=[
        DataRequired(),
        EqualTo("password", message="Passwords must match."),
    ],
  )
  submit = SubmitField(label=('Alterar Senha'))

  # def __init__(self,*k,**kk):
  #   self._user=None #for internal user storing
  #   super(LoginForm,self).__init__(*k,**kk)

  # def validate(self):
  #   self._user=User.query.filter(User.email==self.email.data).first()
  #   return super(LoginForm,self).validate()

  # def validate_email(self,field):
  #   if self._user is None:
  #       raise ValidationError(_("E-Mail not recognized"))


  # def validate_password(self,field):
  #   if self._user is None:
  #       raise ValidationError() #just to be sure
  #   if not self._user.validate_password(self.password.data): #passcheck embedded into user model
  #       raise ValidationError(_("Password incorrect"))
