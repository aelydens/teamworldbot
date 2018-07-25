from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class EncryptForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    multiplier = StringField('Multiplier')
    key = SelectField(label='Key', choices=[('rocket',':rocket:'), ('sandwich',':sandwich:')])
    submit = SubmitField('Encrypt Me!')

class DecryptForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Decrypt Me!')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
