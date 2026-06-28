# Game Recommender API

A video game recommendation engine built with Python and Flask, that takes a user's enjoyed games, and recommends similar games based on their genre and tags.

## How it Works
1. Game data is fetched from the RAWG API and stored in a PostgreSQL database
2. Each game is converted into a numeric feature vector using one-hot encoded genres and tags, and normalized rating and playtime
3. A KNN model finds the most similar games based on cosine similarity
4. Recommendations are served via a Flask REST API

## Tech Stack
- Python
- Flask
- scikit-learn
- PostgreSQL
- RAWG API

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a PostgreSQL database called `game_recommender`
4. Create a `.env` file in the root directory:
```
RAWG_API_KEY=your_rawg_api_key
DB_PASSWORD=your_postgres_password
```
5. Run the API: `python src/api.py` — this will auto-populate the database on first run

## Usage

Start the server:
```bash
python src/api.py
```

Then send a request:
```python
import requests

response = requests.post("http://localhost:5000/recommend",
                         json={"games": ["Elden Ring"]})
print(response.json())
```

## Example Response
```json
{
    "recommendations": [
        "Dark Souls II",
        "Dark Souls III",
        "Dark Souls II: Scholar of the First Sin",
        "Dark Souls: Remastered",
        "Dragon Age: Inquisition"
    ]
}
```

## Future Features
- Average feature vectors of multiple input games for more accurate cross-game recommendations
- Weight key features (genre, specific tags) more heavily to improve recommendation quality