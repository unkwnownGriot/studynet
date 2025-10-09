from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,BooleanField,SubmitField,StringField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from app import db
from app.models import User
import sqlalchemy as sa


class LoginForm(FlaskForm):
    email = EmailField('Enter your email',validators=[DataRequired(),Email()])
    password = PasswordField('Enter your password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Choose a strong password',validators=[DataRequired()])
    confirm_password = PasswordField('Repeat password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    # checking if email is unique
    def validate_email(self,email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data ))
        if user is not None:
            raise ValidationError('Please use a different email address')