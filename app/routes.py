from flask import render_template, flash, redirect, url_for, json
from app import app
from app.forms import EncryptForm, DecryptForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from app.cody import add_two
from app.emoji_class import emoji_it
import random
import emoji
import string
import sys
import os
#from app.emoji_class import *

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

        #received message from form

        message = form.message.data
        multiplier = form.multiplier.data
        # choice = form.key.data
        # options = {u'U+1F680' : ':rocket:', u'U+1F4DC' : ':scroll:')}
        key = form.key.data

        #instantiate class
        emoji_encrypt_class = emoji_it()

        #rewrite message with encrypted message
        emoji_encrypt_class.emoji_key = key
        emoji_encrypt_class.multiplier = multiplier
        message = emoji_encrypt_class.encrypt(message)

        flash('Successfully encrypted!')

        return render_template('encrypt.html', form=form, message=message)

    return render_template('encrypt.html', form=form)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    form = DecryptForm()
    if form.validate_on_submit():

        #received message from form
        message = form.message.data
        multiplier = form.multiplier.data
        # choice = form.key.data
        # options = {u'U+1F680' : ':rocket:', u'U+1F4DC' : ':scroll:')}
        key = form.key.data

        #instantiate class
        emoji_encrypt_class = emoji_it()

        #rewrite message with encrypted message
        emoji_encrypt_class.emoji_key = key
        emoji_encrypt_class.multiplier = multiplier
        message = emoji_encrypt_class.decrypt(message)

        flash('Successfully decrypted!')
        return render_template('decrypt.html', form=form, message=message)

    return render_template('decrypt.html', form=form)

@app.route('/game', methods=['GET', 'POST'])
def game():
    json_url = os.path.join(os.path.realpath(os.path.dirname(__file__)), "static", "puzzles.json")
    puzzles = json.load(open(json_url))

    puzzle_index = random.randint(0, len(puzzles) - 1)
    puzzle = puzzles[puzzle_index]

    #hot swap the 'encrypted' message.
    message = puzzle['decrypted']
    multiplier = random.randint(1, 100)

    emoji_encrypt_class = emoji_it()
    emoji_encrypt_class.multiplier = multiplier
    message = emoji_encrypt_class.encrypt(message)

    puzzle['encrypted'] = message

    return render_template('game.html', puzzle=puzzle)
