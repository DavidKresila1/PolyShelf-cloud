import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)


app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'data')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    SESSION_COOKIE_PATH='/',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db = SQLAlchemy(app)
login = LoginManager()

# ------------------------------- controller imports -----------------------------------------
#
# Each of them is abstracted as blueprints specific to their tasks

from app.controllers.main import main
from app.controllers.auth import auth 

# Registering imported Blueprints

app.register_blueprint(main)
app.register_blueprint(auth)


# ------------------------------- Initialising DB -------------------------------------------

db.init_app(app)
db.create_all()
login.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(_):
    '''404'''
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
