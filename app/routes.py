from flask import render_template, flash, redirect
from app import app
from app.forms import EncryptForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    form = EncryptForm()
    if form.validate_on_submit():
        flash('Encrypting... {}'.format(form.message.data))
        return redirect(url_for('index'))

    return render_template('encrypt.html', form=form)
