from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

POSTGRES = {
    'user': 'user',
    'pw': 'password',
    'db': 'documentation',
    'host': 'localhost',
    'port': '5432',
}


# -- CONFIG DATABASE --
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'bxx7_v%ll=!t5@6a-b*sej%(e3)vqei8od#noicg1x+tjzp^e-'
# Flask-User settings
app.config['USER_APP_NAME'] = "Documentation Ultime"  # Shown in and email templates and page footers
app.config['USER_ENABLE_EMAIL'] = False  # Disable email authentication
app.config['USER_ENABLE_USERNAME'] = True  # Enable username authentication
app.config['USER_REQUIRE_RETYPE_PASSWORD'] = False  # Simplify register form
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models
from app import admin

db.init_app(app)

