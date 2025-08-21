from datetime import datetime

class User:
    def __init__(self,username):
        self.username = username
        self.posts = []

    def create_post(self, content, feed):
        post = Post(self, content)
        self.posts.append(post)
        feed.add_post(post)
        print(f"{self.username} created a post: {content}")

    def like_post(self, post):
        post.add_like()
        print(f"{self.username} liked a post by {post.author.username}")

    def comment_post(self, post, content):
        comment = Comment(self, content)
        post.add_comment(comment)
        print(f"{self.username} commented on a post by {post.author.username}: {content}")

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []
        self.likes = 0
        self.timestamp = datetime.now()

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self):
        self.likes += 1

class Comment:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()

class Feed:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return sorted(self.posts, key=lambda p: p.timestamp, reverse=True)        

    def display_feed(self):
        print("\n--- Social Media Feed ---\n")
        for post in self.get_posts():
            print(f"{post.author.username} posted: {post.content} (Likes: {post.likes})")
            for comment in post.comments:
                print(f" - {comment.user.username}: {comment.content}")
            print()