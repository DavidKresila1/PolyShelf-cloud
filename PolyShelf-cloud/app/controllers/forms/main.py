from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField

class UploadFile(FlaskForm):
    file = FileField('file', validators=[DataRequired()])
    submit = SubmitField('Pridaj súbor')

class CreateDir(FlaskForm):
    dir_name = StringField('Vložte názov priečinka ktorý chcete vytvoriť:', validators=[DataRequired()])
    submit = SubmitField('Vytvor priečinok')

class ChangeDir(FlaskForm):
    dir_name = StringField('Názov priečinku', validators=[DataRequired()])
    submit = SubmitField('Vytvor priečonok')
