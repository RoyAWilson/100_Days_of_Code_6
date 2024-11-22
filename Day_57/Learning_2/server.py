import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url, timeout=5).json()
    return render_template('blog.html', posts=response)

# Challenge issued to print out only blog posts with an ID of 2 - Tutor does by modifying previous.


@app.route('/ifstatement')
def ifstatement():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url, timeout=5).json()
    return render_template('ifstatement.html', posts=response)


if __name__ == '__main__':
    app.run()
