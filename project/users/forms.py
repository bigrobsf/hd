from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, BooleanField

class NewUserForm(FlaskForm):
    username = StringField('User Name', [validators.Length(min=3)])
    password = PasswordField('Password', [validators.InputRequired(), validators.EqualTo('confirm', 
                                                                message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    first_name = StringField('First Name', [validators.Length(min=3)])
    last_name = StringField('Last Name', [validators.Length(min=1)])
    admin = BooleanField('Admin?')

class UpdateUserForm(FlaskForm):
    username = StringField('User Name', [validators.Length(min=3)])
    first_name = StringField('First Name', [validators.Length(min=3)])
    last_name = StringField('Last Name', [validators.Length(min=1)])
    admin = BooleanField('Admin?')

class LoginForm(FlaskForm):
    username = StringField('User Name', [validators.Length(min=3)])
    password = PasswordField('Password', [validators.Length(min=3)])

class DeleteForm(FlaskForm):
    pass