import os

from flask import Blueprint, render_template, abort, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
import psutil
from jinja2 import TemplateNotFound
from flask_admin.contrib.sqla import ModelView
import socketio
from flask_admin import Admin
from app import db, login, app

from app.models.user import User

from app.controllers.forms.auth import LoginForm, SignupForm

admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')

admin = Admin(app, name='Dashboard')
admin.add_view(ModelView(User, db.session))


def getStats():
    cpu = psutil.cpu_stats()