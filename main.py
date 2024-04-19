from flask import Flask, render_template
import requests
from post import Post


blog_url = "https://api.npoint.io/15098e959ebff5d1f390"
response = requests.get(blog_url)
all_posts_data = response.json()
all_posts = []
for post in all_posts_data:
    post_entry = Post(post_id=post["id"],title=post["title"],subtitle=post["subtitle"], body=post["body"])
    all_posts.append(post_entry)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:num>')
def get_post(num):
    return render_template("post.html", posts=all_posts, id=num)


if __name__ == "__main__":
    app.run(debug=True)
