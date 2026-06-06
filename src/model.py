from sklearn.neighbors import NearestNeighbors

class GameRecommender:
    def __init__(self):
        self.model = None
    
    def fit(self, feature_matrix):
        # fits KNN model on the feature matrix
        pass
    
    def recommend(self, game_name, games_df, feature_matrix, n):
        # returns n recommended games based on game_name
        pass