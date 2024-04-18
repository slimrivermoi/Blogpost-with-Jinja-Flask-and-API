from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/15098e959ebff5d1f390"
response = requests.get(blog_url)
all_posts = response.json()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=all_posts, id=num)


if __name__ == "__main__":
    app.run(debug=True)
