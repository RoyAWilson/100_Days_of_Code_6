import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
import smtplib


load_dotenv()

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

from_add = os.getenv('FROM_EMAIL')
from_pass = os.getenv('FROM_PASSWORD')
to_mail = os.getenv('TO_EMAIL')

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        # Set up and send outward email
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {
        name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(from_add, from_pass)
        connection.sendmail(from_add, to_mail, email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)