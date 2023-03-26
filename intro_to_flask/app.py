from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('jinja_intro.html', name='Bob Smith', template_name='Jinja2')
