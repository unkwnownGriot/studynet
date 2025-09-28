from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email


class LoginForm(FlaskForm):
    email = EmailField('Enter your email',validators=[DataRequired(),Email()])
    password = PasswordField('Enter your password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')