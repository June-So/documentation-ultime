from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# -- CONFIG DATABASE --
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = True

db = SQLAlchemy(app)

from app import views, models

db.init_app(app)
models.db_init(db)
