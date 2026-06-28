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
    # Read incoming JSON request
    data = request.get_json()
    games = data.get("games")

    if not games:
        return jsonify({"error": "No games provided."}), 400

    # TODO: improve to average feature vectors of all input games and run KNN once on the combined vector instead of looping
    # Get recommendations for each input game
    recommendations = []
    for game in games:
        rec = recommender.recommend(game, games_df, feature_matrix, 5)
        recommendations.extend(rec)
    
    # Remove duplicates while preserving order
    recommendations_set = list(dict.fromkeys(recommendations))

    return jsonify({"recommendations": recommendations_set})

if __name__ == "__main__":
    app.run(debug=True)