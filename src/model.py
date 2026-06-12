from sklearn.neighbors import NearestNeighbors

class GameRecommender:
    def __init__(self):
        self.model = None
    
    def fit(self, feature_matrix, n_neighbors = 11):
        # fits KNN model on the feature matrix
        self.model = NearestNeighbors(n_neighbors=n_neighbors, metric='cosine')
        self.model.fit(feature_matrix)
    
    def recommend(self, game_name, games_df, feature_matrix, n):
        # Returns n recommended games based on game_name

        # Find the index of the game within games_df
        game_index = games_df[games_df['name'] == game_name].index[0]

        # Find its respective vector within the feature matrix
        game_vector = feature_matrix.iloc[game_index]

        # Find the nearest
        distances, indices = self.model.kneighbors([game_vector])

        # Convert indices into game names
        recommended = games_df.iloc[indices[0]]['name'].tolist()

        # Remove the input game and return the top n recommendations
        recommended = [name for name in recommended if name != game_name]
        return recommended[:n]