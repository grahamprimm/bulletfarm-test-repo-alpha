import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection_pool = []
        self.pool_size = 5
        self._initialize_connection_pool()

    def _initialize_connection_pool(self):
        for _ in range(self.pool_size):
            conn = self.create_connection()
            if conn:
                self.connection_pool.append(conn)

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        return conn

    def get_connection(self):
        if self.connection_pool:
            return self.connection_pool.pop()
        else:
            return self.create_connection()

    def release_connection(self, conn):
        self.connection_pool.append(conn)

    def close_all_connections(self):
        for conn in self.connection_pool:
            conn.close()