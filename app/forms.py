from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class EncryptForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Encrypt Me!')

class DecryptForm(FlaskForm):
    #message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Decrypt Me!')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
