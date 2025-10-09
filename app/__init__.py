from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

# database instance initialization
db = SQLAlchemy(flask_app)

# migration instance initialization
migrate = Migrate(flask_app,db)

# flask-login instance initialization
login = LoginManager(flask_app)
login.login_view = 'login'

from app import routes,models,forms