import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "Models")

movies = pickle.load(
    open(os.path.join(MODEL_DIR, "user_movie_list.pkl"), "rb")
)

similarity = pickle.load(
    open(os.path.join(MODEL_DIR, "similarity.pkl"), "rb")
)

def recommend(movie,n=5):

    movie=movie.lower()

    titles=movies[
        'title'
    ].str.lower()

    if movie not in titles.values:

        return "Movie not found"

    idx=movies[
        titles==movie
    ].index[0]

    distances=list(
        enumerate(
            similarity[idx]
        )
    )

    movie_list=sorted(

        distances,

        reverse=True,

        key=lambda x:x[1]

    )[1:n+1]


    recommendations=[]

    for i in movie_list:

        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations




movie_name = "intrusion"

print("Searching for:", movie_name)

titles = movies["title"].str.lower()

print(movie_name.lower() in titles.values)