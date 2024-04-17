import sqlite3

from src.creational.singleton.singleton import Singleton


class DatabaseConnection(Singleton):
    _connection = None

    def __init__(self):
        if self._connection is None:
            self._connection = sqlite3.connect('users.db')

    def execute_query(self, query):
        if self._connection is None:
            raise Exception("No connection")
        cursor = self._connection.execute(query)
        cursor.execute(query)
        self._connection.commit()

    def disconnect(self):
        if self._connection is not None:
            self._connection.close()
            self._connection = None


db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Joe')")

print(db1 is db2)
db1.disconnect()
db2.disconnect()
