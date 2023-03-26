import datetime
import json
from flask import Flask, render_template, request
from pymongo import MongoClient

with open('secrets.json', 'r') as read_file:
    secrets = json.load(read_file)

app = Flask(__name__)
client = MongoClient(secrets["MONGODB_URL"])
app.db = client.microblog

entries = []


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entry_content = request.form.get('content')
        formatted_date = datetime.datetime.today().strftime('%Y-%m-%d')
        entries.append((entry_content, formatted_date))
        app.db.entries.insert(
            {'content': entry_content, 'date': formatted_date})

    entries_with_date = [
        (entry['content'], entry['date'], datetime.datetime.strptime(entry[1], '%Y-%m-%d').strftime('%b %d')) for entry in entries
    ]
    return render_template('home.html', entries=entries_with_date)
