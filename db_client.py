import psycopg2
import os
class DBClient:
    def __init__(self):
        host = os.getenv("DB_HOST", "localhost")
        self.connection = psycopg2.connect(
            host=host,
            port=5432,
            user="qa_user",
            password="qa_pass",
            database="qa_database"
        )
        self.connection.autocommit = True

    def fetch(self, query):
        cur = self.connection.cursor()
        cur.execute(query)
        return cur.fetchall()

    def execute(self, query):
        cur = self.connection.cursor()
        cur.execute(query)

    def close(self):
        self.connection.close()