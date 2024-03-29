/Users/mac/Documents/flask_proj

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '141448041aadf99c8df7583f2872710c'

posts = [
    {
        'author': 'Tempah',
        'title': 'Blog post1',
        'content': 'first post sucks',
        'date_posted': 'March 6'
    },
    {
        'author': 'Tempah',
        'title': 'Blog post2',
        'content': 'second post sucks',
        'date_posted': 'Sep 22'
    }
]

@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/')
def hello_world():
    return '<h1>Hello world!</h1>'

@app.route('/about')
def about():
    return render_template('about.html', title='about')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Sign Up', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('Login.html', title='Login', form=form)

@app.route('/python/<text>', strict_slashes=False)
def display_text(text='cool'):
    return 'python ' + text.replace('_', ' ')

@app.route('/number/<n>')
def display_number(n):
    try:
        int_n = int(n)
        return f'{n} is a number'
    except ValueError:
        raise ValueError(f'{n} is not a number')
    
@app.route('/number_template/<n>')
def display_number_1(n):
    try:
        int_a = int(n)
        return render_template('5-number.html')
    except ValueError:
        raise ValueError(f'{n} is not a number')

@app.route('/number_odd_or_even/<n>')
def display_number_odd(n):
    number_type = "even" if int(n) % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', number=n, number_type=number_type)





if __name__ == '__main__':
    app.run(debug=True)
/Users/mac/Documents/flask_proj

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('error!', response.status_code)
/Users/mac/Documents/flask_proj

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

/Users/mac/Documents/flask_proj


