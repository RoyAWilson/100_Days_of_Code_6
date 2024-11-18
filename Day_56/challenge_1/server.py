''''
Challenge - Add a CSS file to change the background colour to purple on a simple website
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
