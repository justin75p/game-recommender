import requests
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("RAWG_API_KEY")

def fetch_games(num_pages: int, page_size: int):
    # Returns a list of the most popular games from the RAWG database.
    
    # Parameters:
        # num_pages (int): The number of pages to fetch.
        # page_size(int): The entries per page to fetch.

    # Returns:
        # list of dictionary: A list of games, where each game is a dictionary, with:
            # - id (int): RAWG game ID
            # - name (str): Game title
            # - rating (float): RAWG user rating (0-5)
            # - playtime (int): Average playtime in hours
            # - metacritic (int): Metacritic score (0-100)
            # - genres (list of str): List of genre names e.g. ["Action", "RPG"]
            # - tags (list of str): List of tag names e.g. ["Open World", "Singleplayer"]
    games = []

    for page in range(1, num_pages + 1):
        response = requests.get("https://api.rawg.io/api/games", params = {
            "key": API_KEY,
            "page_size": page_size,
            "page": page,
            # Order by popularity
            "ordering": "-added"
        })

        data = response.json()

        for game in data['results']:
            games.append({
                'id': game['id'],
                'name': game['name'],
                'rating': game['rating'],
                'playtime': game['playtime'],
                'metacritic': game['metacritic'],
                'genres': [g['name'] for g in game['genres']],
                'tags': [t['name'] for t in game['tags']]
            })

    return games

def save_to_db():
    # TODO: saves a list of games into database
    return None