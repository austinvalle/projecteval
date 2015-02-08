from flask.ext.wtf import Form

from wtforms import TextField, PasswordField, HiddenField, DateTimeField, TextAreaField, StringField

from wtforms.validators import Required, Email, EqualTo, url, Length

class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [Required(message='Must provide a password.')])

class RegisterForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Please enter valid email')])
    username = TextField('Username', [Required(message='Please enter a username')])
    password = PasswordField('Password', [Required(message='Must provide a password')])

class EditGameForm(Form):
    id = HiddenField('Game Id', [Required(message='Need a game id')])
    releaseDate = DateTimeField('Release Date', [Required(message='Please enter a release date')], format='%m/%d/%y')
    description = TextField('Description', [Required(message='Please enter a description')])
    developer = TextField('Developer', [Required(message='Please enter a developer')])
    publisher = TextField('Publisher', [Required(message='Please enter a publisher')])
    trailerUrl = TextField('Trailer Url', [url(message='Must be a url'), Required(message='Please enter a trailer url')])
    title = TextField('Title', [Required(message='Please enter a title')])
