from my_app.config.mysql_config import connect_to_mysql

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.name = data["name"]

    @classmethod
    def get_all(cls):
        query = "select * from users"
        users_from_db = connect_to_mysql('blog').query_db(query)

        my_users = []
        for user in users_from_db:
            my_users.append(cls(user))
        return my_users

    @classmethod
    def get_my_user(cls, data):
        query = "select * from users where email = %(email)s"
        my_user_from_db = connect_to_mysql('blog').query_db(query, data)
        if len(my_user_from_db) == 0:
            return None
        my_user_obj = cls(my_user_from_db[0])
        return my_user_obj

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (email, name) values (%(email)s, %(name)s)"
        my_user_id = connect_to_mysql("blog").query_db(query, data)
        return my_user_id


