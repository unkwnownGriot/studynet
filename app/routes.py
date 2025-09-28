from app import flask_app
from flask import render_template,flash,redirect
from app.forms import LoginForm


@flask_app.route("/")
@flask_app.route("/index")
def index():
    user = {'username':'john'}
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
    return render_template('index.html',title="Home",user=user, posts=posts)

@flask_app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('A user tried to login with this email: {}, \
              should we remember him ? {}'.format(form.email.data, 
                                                    form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',form=form,title='Sign In')