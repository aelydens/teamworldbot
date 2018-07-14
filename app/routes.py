from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import EncryptForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.cody import add_two
import emoji
import string
import sys
from app.emoji_class import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    form = EncryptForm()
    if form.validate_on_submit():

        emoji_list = list(emoji.EMOJI_UNICODE)
        alphabet_lower = string.ascii_lowercase
        # Encryption should happen here:
        # message = emojify.encrypt(form.message.data)
        # with error handling & messages to user
        message = form.message.data

        message = str(add_two(int(message)))

        flash('Successfully encrypted!')

        return render_template('encrypt.html', form=form, message=message)

    return render_template('encrypt.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid login credentials')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('admin'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
