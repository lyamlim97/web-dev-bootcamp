from flask import Flask, render_template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route('/')
def hello_world():
    return render_template('jinja_intro.html', name='Bob Smith', template_name='Jinja2')


@app.route('/expressions/')
def render_expressions():

    # interpolation
    color = 'brown'
    animal_one = 'fox'
    animal_two = 'dog'

    # addition and subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = 'Captain'
    last_name = 'Marvel'

    # group as dictionary
    kwargs = {
        'color': color,
        'animal_one': animal_one,
        'animal_two': animal_two,
        'orange_amount': orange_amount,
        'apple_amount': apple_amount,
        'donate_amount': donate_amount,
        'first_name': first_name,
        'last_name': last_name
    }

    return render_template('expressions.html', **kwargs)


@app.route('/data-structures/')
def render_data_structures():

    # lists
    movies = [
        'Leon the Professional',
        'The Usual Suspects',
        'A Beautiful Mind'
    ]

    # dictionary
    car = {
        'brand': 'Tesla',
        'model': 'Roadster',
        'year': '2020'
    }

    # custom data structure (class)
    moons = GalileanMoons('Io', 'Europa', 'Ganymede', 'Callisto')

    kwargs = {
        'movies': movies,
        'car': car,
        'moons': moons,
    }

    return render_template('data_structures.html', movies=movies, car=car, moons=moons)


@app.route('/conditionals-basics/')
def render_conditionals():
    company = 'Microsoft'

    return render_template('conditionals_basics.html', company=company)


@app.route('/for-loop/')
def render_loops_for():
    planets = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupyter',
        'Saturn',
        'Uranus',
        'Neptune'
    ]

    return render_template('for_loops.html', planets=planets)


@app.route('/for-loop/conditionals/')
def render_for_loops_conditionals():
    user_os = {
        'Bob Miller': 'Windows',
        'Judy Lee': 'MacOS',
        'Zach Ng': 'Linux',
        'Regina George': 'Windows'
    }

    return render_template('loops_and_conditionals.html', user_os=user_os)
