from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()] )
    senha = PasswordField("Senha", validators=[DataRequired()] )
    botao_confirmacao = SubmitField("Fazer Login")


class FormCriarContra(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()] )
    username = StringField("Nome de usuário", validators=[DataRequired()] )
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)] )
    confirmar_senha = PasswordField("Confirmação Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")


def validate_email(self, email):
    usuario = Usuario.query.filter_by(email=email.data).first()
    if usuario:
        return ValidationError("Email já cadastrado, faça login para continuar")

    
    
