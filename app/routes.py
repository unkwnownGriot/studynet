from app import flask_app
from flask import render_template


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