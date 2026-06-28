from flask import Flask, request, jsonify
from database import Database
from features import build_feature_matrix
from model import GameRecommender

app = Flask(__name__)

@app.route("/recommend", methods = ["POST"])
def recommend():
    return jsonify({})