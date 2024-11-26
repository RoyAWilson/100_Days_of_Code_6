import json
import requests

from flask import Flask
from flask import render_template, url_for

blog_data = requests.get(
    url='https://api.npoint.io/62030efdfbae91083277', timeout=15).json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=blog_data)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for b_post in blog_data:
        if b_post['id'] == index:
            requested_post = b_post
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
