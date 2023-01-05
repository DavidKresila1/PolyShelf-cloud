import os

from flask import Blueprint, render_template, abort, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from jinja2 import TemplateNotFound
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from app import db, login, app

from app.models.user import User

from app.controllers.forms.auth import LoginForm, SignupForm

auth = Blueprint('auth', __name__, template_folder='templates')

admin = Admin(app, name='Dashboard')
admin.add_view(ModelView(User, db.session))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@auth.context_processor
def user_auth():
    def is_logged_in():
        return current_user.is_authenticated
    return dict(is_logged_in=is_logged_in)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/drive')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nesprávne meno alebo heslo')
        else:
            login_user(user, remember=form.remember_me.data)
        return redirect('login')
    return render_template("login.html", form=form, title='Prihlásenie')



@auth.route('/register', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect('/drive')
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            if form.password.data == form.confirm_password.data:

                
                new_user = User(form.username.data, form.email.data, form.password.data)
                db.session.add(new_user)
                db.session.commit()


                user_space = os.makedirs(app.config['UPLOAD_FOLDER'] + "/" + str(new_user.id))
                   
                return redirect(url_for('auth.login'))
            flash("Heslá sa nezhodujú")
        else:
            flash("Email sa už používa")
    return render_template("register.html", form=form, title="Registrácia")
            
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
