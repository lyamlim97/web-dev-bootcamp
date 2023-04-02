import functools

from flask import (Flask, abort, flash, redirect, render_template, request,
                   session, url_for)
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
# secret key generated with secrets.token_urlsafe()
app.secret_key = 'lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA'

users = {}


def login_requried(route):
    @functools.wraps(route)
    def route_wrapper(*args, **kwargs):
        email = session.get('email')
        if email or email not in users:
            return redirect(url_for('login'))

        return route(*args, **kwargs)

    return route_wrapper


@app.get('/')
def home():
    return render_template('home.html', email=session.get('email'))


@app.get('/protected')
@login_requried
def protected():
    if not session.get('email'):
        abort(401)
    return render_template('protected.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = ''

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if users.get(email) != None:
            if pbkdf2_sha256.verify(password, users.get(email)):
                session['email'] = email
                return redirect(url_for('protected'))
        else:
            abort(401)
    return render_template('login.html', email=email)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        users[email] = pbkdf2_sha256.hash(password)
        session['email'] = email

        flash('Successfully signed up.')
        return redirect(url_for('login'))

    return render_template('signup.html')
