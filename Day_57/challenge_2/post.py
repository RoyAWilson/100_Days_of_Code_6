import requests

URL = "https://api.npoint.io/c10781c59f247ee64d13"


class Post:
    def get_post(self, index=None):
        all_posts = requests.get(url=URL, timeout=5).json()
        if index is not None:
            return all_posts
        return all_posts
