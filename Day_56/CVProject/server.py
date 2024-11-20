from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


@app.route('/image1')
def image1():
    return render_template('image1.html')


@app.route('/image2')
def image2():
    return render_template('image2.html')


@app.route('/image3')
def image3():
    return render_template('image3.html')


@app.route('/image4')
def image4():
    return render_template('image4.html')


if __name__ == '__main__':
    app.run(debug=True)
