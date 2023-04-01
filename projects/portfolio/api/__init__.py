from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'name': 'Habit tracking app with Python and MongoDB',
        'thumb': 'img/habit-tracking.png',
        'hero': 'img/habit-tracking-hero.png',
        'categories': ['python', 'mongodb'],
        'slug': 'habit-tracking',
        'prod': 'www.google.com',
    },
    {
        'name': 'Microblog app with Python and MongoDB',
        'thumb': 'img/personal-finance.png',
        'hero': 'img/personal-finance.png',
        'categories': ['python', 'mongodb', 'writing'],
        'slug': 'microblog',
        'prod': 'www.google.com',
    }
]


@app.route('/')
def home():
    return render_template('home.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
