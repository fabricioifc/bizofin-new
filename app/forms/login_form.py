from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError


class LoginForm(FlaskForm):
  email = EmailField("E-mail", validators=[DataRequired(), Email(message=None)])
  password = PasswordField("Senha", validators=[DataRequired()])

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
