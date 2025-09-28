from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

flask_app = Flask(__name__)
flask_app.config.from_object(Config)

# database instance initialization
db = SQLAlchemy(flask_app)

# migration instance initialization
migrate = Migrate(flask_app,db)

from app import routes,models,forms