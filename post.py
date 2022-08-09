class Post:
    def __init__(self, author, title, content):
        self.post_author = author
        self.post_title = title
        self.post_content = content

    def get_post_info(self):
        print(f"{self.post_title} is written by {self.post_author}. Post: {self.post_content}")

