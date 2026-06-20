import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "Models")

movies = pickle.load(
    open(os.path.join(MODEL_DIR, "user_movie_list.pkl"), "rb")
)

hybrid_scores = pickle.load(
    open(os.path.join(MODEL_DIR, "hybrid.pkl"), "rb")
)



def hybrid_recommend(movie, n=5):

    if movie is None:
        return []

    movie = str(movie).lower().strip()

    titles = movies["title"].str.lower()

    matches = movies[titles == movie]

    if matches.empty:
        return ["Movie not found"]

    idx = matches.index[0]

    distances = list(enumerate(hybrid_scores[idx]))

    movies_list = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )[1:n+1]

    recommendations = [
        movies.iloc[i[0]]["title"]
        for i in movies_list
    ]

    return recommendations



if __name__ == "__main__":
    print(hybrid_recommend("intrusion"))
    print("\nRecommendations:")
    print(hybrid_recommend("the starling"))