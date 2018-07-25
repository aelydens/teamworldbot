from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired


class EncryptForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    multiplier = IntegerField('Multiplier', default=1)
    key = SelectField(label='Key', choices=[(':rocket:','🚀'), (':scroll:','📜'), (':bank:': '🏦'), (':hot_dog:': '🌭'), (':ogre:': '👹'), (':sailboat:': '⛵'), (':doughnut:': '🍩'), (':bus:': '🚌')])
    submit = SubmitField('Encrypt Me!')

class DecryptForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    multiplier = IntegerField('Multiplier', default=1)
    key = SelectField(label='Key', choices=[(':rocket:','🚀'), (':scroll:','📜'), (':bank:': '🏦'), (':hot_dog:': '🌭'), (':ogre:': '👹'), (':sailboat:': '⛵'), (':doughnut:': '🍩'), (':bus:': '🚌')])
    submit = SubmitField('Decrypt Me!')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
