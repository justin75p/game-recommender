import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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

    # Convert the list of tuples into a DataFrame, split the genres and tags into lists
    games_df = pd.DataFrame(games, columns=['id', 'name', 'rating', 'playtime', 'metacritic', 'added', 'genres', 'tags'])
    games_df['genres'] = games_df['genres'].str.split(',').fillna('').apply(list)
    games_df['tags'] = games_df['tags'].str.split(',').fillna('').apply(list)

    # Filter to top 50 most common tags
    all_tags = games_df['tags'].explode()
    top_50_tags = all_tags.value_counts().head(50).index

    filtered_tags = []
    for tag_list in games_df['tags']:
        filtered = [tag for tag in tag_list if tag in top_50_tags]
        filtered_tags.append(filtered)

    games_df['tags'] = filtered_tags

    # One-hot encode genres column
    genres_dummies = games_df['genres'].explode()
    genres_dummies = pd.get_dummies(genres_dummies).groupby(level=0).max().astype(int).add_prefix('genre_')

    # One-hot encode tags column
    tags_dummies = games_df['tags'].explode()
    tags_dummies = pd.get_dummies(tags_dummies).groupby(level=0).max().astype(int).add_prefix('tag_')

    # Normalize the rating and playtime columns
    scaler = MinMaxScaler()
    rating_playtime = games_df[['rating', 'playtime']]
    normalized = pd.DataFrame(scaler.fit_transform(rating_playtime), columns = ['rating', 'playtime'])

    feature_matrix = pd.concat([normalized, genres_dummies, tags_dummies], axis=1)

    return feature_matrix, games_df