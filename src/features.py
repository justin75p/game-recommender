import pandas as pd

def build_feature_matrix(games):
    """
    Transforms raw game data from the database into a numeric feature matrix for KNN.

    Parameters:
        games (list of tuples): Raw game data from get_all_games()
            Each tuple: (id, name, rating, playtime, metacritic, added, genres, tags)

    Returns:
        feature_matrix (DataFrame): Numeric matrix ready for KNN
        games_df (DataFrame): Original game data with names and ids for lookup
    """

    games_df = pd.DataFrame(games, columns=['id', 'name', 'rating', 'playtime', 'metacritic', 'added', 'genres', 'tags'])
    games_df['genres'] = games_df['genres'].str.split(',')
    games_df['tags'] = games_df['tags'].str.split(',')

    return games_df