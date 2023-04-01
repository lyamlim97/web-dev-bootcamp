import os

from flask import (Flask, abort, flash, redirect, render_template, request,
                   session, url_for)

app = Flask(__name__)
# secret key generated with secrets.token_urlsafe()
app.secret_key = 'lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA'

users = {}


@app.get('/')
def home():
    return render_template('home.html', email=session.get('email'))


@app.get('/protected')
def protected():
    if not session.get('email'):
        abort(401)
    return render_template('protected.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        users[email] = password
        session['email'] = email
        flash('Successfully signed up.')
        return redirect(url_for('home'))

    return render_template('signup.html')
