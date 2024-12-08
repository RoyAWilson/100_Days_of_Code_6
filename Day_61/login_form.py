"""
    Build a user form for display by Flask.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, Length, Email


class LoginForm(FlaskForm):
    """_summary_

    Args: 
        FlaskForm (_type_): _description_
    To build a user input form for use with Flask etc.
    """
    email = StringField(label='Email', validators=[data_required(), Email()])
    password = PasswordField(label='Password', validators=[
                             data_required(), Length(min=8)])
    submit = SubmitField(label='Log In')
