from flask import Flask, render_template
from post import Post


app = Flask(__name__)


@app.route('/')
def home():
    posts = Post()
    all_blogs = posts.get_post()
    return render_template("index.html", posts=all_blogs)


@app.route('/post/<int:number>')
def get_blog(number):
    posts = Post()
    all_blogs = posts.get_post()
    return render_template('post.html', posts=all_blogs, num=number)


if __name__ == "__main__":
    app.run(debug=True)
