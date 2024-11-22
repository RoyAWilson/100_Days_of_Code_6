"""Serves up web pages.

    Returns:
        _type_ None
    """
import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """_summary_
    Opens URL and sends args to api
    Returns:
        URL: returns url with args from api formatted and written to HTML page
    """
    return 'Please enter guess/ and your name in url bar'


@app.route('/guess/<name>')
def guess(name):
    """_summary_
    Opens Guess page when /guess/<name typed in url bar>
    Args:
        name (_type_ int): _description_

    Returns:
        _type_: _description_
    """
    gender_url = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(url=gender_url, timeout=5).json()['gender']
    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(url=age_url, timeout=5).json()['age']
    if age_response > 35:
        message = 'Should I pass you your walking stick and pension book, you old fart?!?'
    else:
        message = 'Isn\'t it past you bedtime, child?!?'
    return render_template('guess.html', name=name,
                           gender=gender_response, age=age_response, message=message)


if __name__ == '__main__':

    app.run(debug=True)
