import datetime
import json
from flask import Flask, render_template, request
from pymongo import MongoClient

with open('secrets.json', 'r') as read_file:
    secrets = json.load(read_file)


def create_app():
    app = Flask(__name__)
    client = MongoClient(secrets["MONGODB_URL"])
    app.db = client.microblog

    @app.route("/", methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            entry_content = request.form.get('content')
            formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')

        entries_with_date = [
            (
                entry['content'],
                entry['date'],
                datetime.datetime.strptime(
                    entry['date'], '%Y-%m-%d').strftime('%b %d')
            )
            for entry in app.db.entries.find({})
        ]

        return render_template('home.html', entries=entries_with_date)

    return app
