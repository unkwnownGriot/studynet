from app import flask_app,db
from flask import render_template,flash,redirect,url_for,request
import sqlalchemy as sa
from app.forms import LoginForm,RegistrationForm
from app.models import User
from urllib.parse import urlsplit
from flask_login import current_user,login_user,login_required,logout_user


@flask_app.route("/")
@flask_app.route("/index")
@login_required
def index():
    posts = [
        {
            'author':{'username':'fred'},
            'body':'post from fred'
        },
        {
            'author':{'username':'sandra'},
            'body':'post from susan'
        }
    ]
    return render_template('index.html',title="Home", posts=posts)

@flask_app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).
                                 where(User.email == form.email.data))
        if not user or not user.check_password_hash(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user=user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('index')
        flash("you've been login succesfully")
        return redirect(next_page)
    return render_template('login.html',form=form,title='Sign In')

@flask_app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password_hash(form.confirm_password.data)
        db.session.add(user)
        db.session.commit()
        flash("User has been registered successfully !")
        return redirect(url_for('login'))
    return render_template('register.html',form=form,title="Register")

@flask_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    