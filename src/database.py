import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Database():
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(
            host="localhost",
            dbname="game_recommender",
            user="postgres",
            password=os.getenv("DB_PASSWORD"), 
            port="5432"
        )

    def close(self):
        if self.conn:
            self.conn.close()

    def save_games(self, games):
        pass

    def get_all_games(self):
        pass