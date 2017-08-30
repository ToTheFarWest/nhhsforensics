from flask_wtf import Form
from wtforms import BooleanField, TextField, validators, PasswordField
from . import UserConstants

class LoginForm(Form):
    username    = TextField('Username', [validators.Required()])
    password    = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('Remember Me', default=False)

class RegisterForm(Form):
    user_name   = TextField('Username',  [
        validators.Length(
            min = UserConstants.MIN_USERNAME_LEN,
            max = UserConstants.MAX_USERNAME_LEN
        ),
        validators.Regexp(
            "^[a-zA-Z0-9]*$",
            message="Username can only contain letters and numbers"
        )
    ])
    first_name  = TextField('First Name', [validators.Required()])
    last_name   = TextField('Last Name', [validators.Required()])
    email       = TextField('E-mail', [validators.Required(), validators.Email()])
    password    = PasswordField(
        'New Password',
        [validators.Length(min=UserConstants.MIN_PASSWORD_LEN, max=UserConstants.MAX_PASSWORD_LEN)]
    )
    confirm     = PasswordField('Repeat Password', [
        validators.Required(),
        validators.EqualTo('password', message='Passwords must match')
    ])
