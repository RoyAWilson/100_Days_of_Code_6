from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    string = f'user: {request.form['username']} pass: {
        request.form['password']}'
    return string


if __name__ == "__main__":
    app.run(debug=True)
