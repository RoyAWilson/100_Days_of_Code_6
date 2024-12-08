from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, Length, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[data_required(), Email()])
    password = PasswordField(label='Password', validators=[
                             data_required(), Length(min=8)])
    submit = SubmitField(label='Log In')
