from fetch_games import fetch_games
from features import build_feature_matrix
from database import Database
from model import GameRecommender

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

# Build feature matrix
feature_matrix, games_df = build_feature_matrix(games)

# Fit the KNN model
recommender = GameRecommender()
recommender.fit(feature_matrix)

# Test recommendation
game = "Elden Ring"
recommendations = recommender.recommend(game, games_df, feature_matrix, 5)

print(f"Because you liked {game}, you might also enjoy:")
for rec in recommendations:
    print(f"  - {rec}")