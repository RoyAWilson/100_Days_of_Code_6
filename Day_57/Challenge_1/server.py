import requests
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return 'Please enter guess/ and your name in url bar'


@app.route('/guess/<name>')
def guess(name):
    gender_url = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_url).json()['gender']
    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url).json()['age']
    if age_response > 35:
        message = 'Should I pass you your walking stick and pension book, you old fart?!?'
    else:
        message = 'Isn\'t it past you bedtime, child?!?'
    return render_template('guess.html', name=name, gender=gender_response, age=age_response, message=message)


if __name__ == '__main__':

    app.run(debug=True)
