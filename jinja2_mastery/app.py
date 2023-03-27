from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def todo():
    todos = ['Get milk', 'Learn programming']
    return render_template('home.html', todos=todos)
