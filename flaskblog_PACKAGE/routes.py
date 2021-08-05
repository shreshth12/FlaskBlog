from flask import render_template, url_for, flash, redirect, request
from sqlalchemy.orm.query import Query
from wtforms.validators import Email
from flaskblog_PACKAGE import app, db, bcrypt
from flaskblog_PACKAGE.forms import RegistrationForm, LoginForm
from flaskblog_PACKAGE.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

data = [
    {'Name' : 'Shreshth',
    'age' : 21,
    'content' : 'Do not give up',
    'weight' : 'I won\'t tell you',
    'date_posted' : '29th July',
    },

    {'Name' : 'Sarthak',
    'age' : 16,
    'content' : 'Do not give up when your in US',
    'weight' : 'I won\'t tell you',
    'date_posted' : '29th July',
    }
]

@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html", post = data, title = 'HOMEPAGE')

@app.route("/about")
def about():
    return render_template("about.html", title = 'ABOUTPAGE')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = pw_hash)
        db.session.add(user)
        db.session.commit()  
        flash("Your account has been created!", 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title = 'REGISTRATION PAGE', form = form)

@app.route("/login",methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'You are now logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('homePage'))
        else:
            flash(f'Wrong credentials, try again', 'danger')
    return render_template("login.html", title = 'LOGIN PAGE', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homePage'))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title = 'ACCOUNT PAGE')