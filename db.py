import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.pool = []

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def get_connection(self):
        if self.pool:
            return self.pool.pop()
        return self.create_connection()

    def release_connection(self, conn):
        self.pool.append(conn)

# Create a single instance of the Database connection pool
database = Database('your_database.db')

def get_connection():
    return database.get_connection()

def release_connection(conn):
    return database.release_connection(conn)
