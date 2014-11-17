from flask.ext.wtf import Form

from wtforms import TextField, PasswordField

from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [Required(message='Must provide a password.')])

class RegisterForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Please enter valid email')])
    username = TextField('Username', [Required(message='Please enter a username')])
    password = PasswordField('Password', [Required(message='Must provide a password')])
