from flask import (
    Flask,
    render_template,
    request
)

import sys
import os

# Add src folder to path
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_DIR = os.path.join(
    BASE_DIR,
    ".."
)

sys.path.append(PROJECT_DIR)

# Import custom modules
from Src.hybrid import hybrid_recommend
from Src.predictor import predict_popularity
from Src.tmdb import fetch_poster


app = Flask(__name__)


# =====================
# Home Page
# =====================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =====================
# Recommendation Route
# =====================

@app.route('/recommend', methods=['POST'])
def recommend():

    movie = request.form.get("movie")

    print("User searched:", movie)

    recommendations = hybrid_recommend(movie)

    # Poster of searched movie
    searched_movie_poster = fetch_poster(movie)

    print("Searched poster:", searched_movie_poster)

    results = []

    for movie_title in recommendations:

        poster = fetch_poster(movie_title)

        print("Movie:", movie_title)
        print("Poster:", poster)

        results.append({
            "title": movie_title,
            "poster": poster
        })
    print(results)

    return render_template(
        "index.html",
        recommendations=results,
        searched_movie=movie,
        searched_poster=searched_movie_poster
    )
    
# =====================
# Popularity Prediction
# =====================

@app.route(
    "/predict_popularity",
    methods=["POST"]
)
def predict():

    vote_count = float(
        request.form.get(
            "vote_count"
        )
    )

    vote_average = float(
        request.form.get(
            "vote_average"
        )
    )

    prediction = predict_popularity(

        vote_count,

        vote_average

    )

    return render_template(

        "predict.html",

        prediction=prediction

    )


# =====================
# Run App
# =====================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000

    )