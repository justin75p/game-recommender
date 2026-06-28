from flask import Flask, request, jsonify
from database import Database
from features import build_feature_matrix
from fetch_games import fetch_games
from model import GameRecommender

app = Flask(__name__)

# Connect to database
db = Database()
db.connect()
db.create_table()

# Fetch games if database is empty
games = db.get_all_games()
if not games:
    print("Database empty, fetching games from RAWG...")
    games_data = fetch_games(25, 40)
    db.save_games(games_data)
    games = db.get_all_games()
db.close()

# Build feature matrix, and fit KNN model
feature_matrix, games_df = build_feature_matrix(games)
recommender = GameRecommender()
recommender.fit(feature_matrix)

@app.route("/recommend", methods = ["POST"])
def recommend():
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)