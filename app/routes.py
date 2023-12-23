from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import logout_user
from flask import request
from urllib.parse import urlsplit
from flask_login import login_required


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home Page' , posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # if user is authenticated then it is not allowed to go to /login
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
    
#     form = LoginForm()

#     # form data is valid or not
#     if form.validate_on_submit():
       
#         #fetching the username from the database
#         user = db.session.scalar(
#             sa.select(User).where(User.username == form.username.data))
        
#         #if no username not exist or password is not matching again rredirect
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
        
#         #register the user as logged in , current_user var will be set to user
#         login_user(user, remember=form.remember_me.data)

#         #if user access a page that require a login and user is not logged in
#         #then send user to login page and then redirect user to user's requested page
#         #next contain that requested page
#         # next_page = request.args.get('next')
#         # if not next_page or urlsplit(next_page).netloc != '':
#         #     next_page = url_for('index')
#         # return redirect(next_page)
    
#     #if form is invalid
#     return render_template('login.html', title='Sign In', form=form)

# from app import app, db
# from app.models import User, Post
# import sqlalchemy as sa
# app.app_context().push()
