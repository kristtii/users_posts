from my_app.config.mysql_config import connect_to_mysql

class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.user_id = data["users_id"]

    @classmethod
    def get_all_posts(cls):
        query = "select * from posts"
        result = connect_to_mysql("blog").query_db(query)
        my_posts = []
        for i in result:
            my_posts.append(cls(i))
        return my_posts

    @classmethod
    def create_post(cls, data):
        query = "insert into posts (content, users_id) values (%(content)s, %(user_id)s)"
        result = connect_to_mysql("blog").query_db(query, data)
        return result

    @classmethod
    def delete_post(cls, data):
        query = "delete from posts where id = %(post_id)s"
        connect_to_mysql("blog").query_db(query, data)
        return

    


