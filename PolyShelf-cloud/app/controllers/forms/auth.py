from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired()])
    remember_me = BooleanField('Pamataj si ma')
    submit = SubmitField('Prihlásiť')

class SignupForm(FlaskForm):
    username = StringField('Používaťeťske meno', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo', validators=[DataRequired(), EqualTo('confirm_password',
                                                                             message='Heslá sa nezhodujú')])
    confirm_password = PasswordField('Potvrď heslo', validators=[DataRequired()])
    submit = SubmitField('Registrácia')
