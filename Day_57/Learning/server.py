import random
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    rand_no = random.randint(1, 10)
    this_year = str(datetime.datetime.now().year)
    return render_template('index.html', num=rand_no, year=this_year)

# Challenge: Create a footer in the HTML document containing text and a copyright year that updates as the year rolls - see above


if __name__ == '__main__':
    app.run(debug=True)
