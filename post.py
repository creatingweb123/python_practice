import requests
class Post:
    def __init__(self):
        self.blog_response = requests.get(url="https://api.npoint.io/39e6830712f42ce02265")
        self.blog_response.raise_for_status()
        self.all_posts = self.blog_response.json()