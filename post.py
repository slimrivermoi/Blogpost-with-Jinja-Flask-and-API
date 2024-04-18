import requests


class Post:

    def get_blog():
        blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(blog_url)
        all_posts = response.json()
        return all_posts
