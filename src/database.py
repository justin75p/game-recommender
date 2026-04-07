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
    def create_table(self):
        if not self.conn:
            print("No connection found. Call connect() first.")
            return
        
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games (\
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                rating REAL,
                playtime INTEGER,
                metacritic INTEGER,
                genres TEXT,
                tags TEXT
            )
        """)

        self.conn.commit()
        cursor.close()

    def close(self):
        if self.conn:
            self.conn.close()

    def save_games(self, games):
        if not self.conn:
            print("No connection found. Call connect() first.")
            return
        
        cursor = self.conn.cursor()
        for game in games:
            cursor.execute("""
                INSERT INTO games (id, name, rating, playtime, metacritic, genres, tags)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (
                game['id'],
                game['name'],
                game['rating'],
                game['playtime'],
                game['metacritic'],
                ','.join(game['genres']),
                ','.join(game['tags'])
                )
            )

        self.conn.commit()
        cursor.close()

    def get_all_games(self):
        if not self.conn:
            print("No connection found. Call connect() first.")
            return
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM games")
        rows = cursor.fetchall()
        cursor.close()

        return rows