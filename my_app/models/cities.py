from my_app.config.mysql_config import connect_to_mysql

class City:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['population']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cities"
        cities_from_db = connect_to_mysql('world').query_db(query)
        cities = []
        for c in cities_from_db:
            cities.append(cls(c))
        return cities

