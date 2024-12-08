"""
    Build a webpage with Flask and flask_bootstrap

    Returns:
        _type_: web page
"""

import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from login_form import LoginForm

app = Flask(__name__)
load_dotenv()
bootstrap = Bootstrap5(app)
app.secret_key = os.getenv('SECRET_KEY')


@app.route("/")
def home():
    """build home page

    Returns:
        HTML doc: Landing page
    """
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Show login page when called for

    Returns:
        HTML: Login page
    """
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == os.getenv('ADMIN_EMAIL') and login_form.password.data == os.getenv('ADMIN_PASS'):
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
