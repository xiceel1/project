import sqlite3


class DataBase:
    def __init__(self, query):
        self.connection = sqlite3.connect('rent.db')
        self.cursor = self.connection.cursor()
        self.query = query

    def db_update(self):
        self.cursor.execute(self.query)

    def __del__(self):
        self.connection.commit()
        self.connection.close()



