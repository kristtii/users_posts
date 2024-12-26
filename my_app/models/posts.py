class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.user_id = data["users_id"]

