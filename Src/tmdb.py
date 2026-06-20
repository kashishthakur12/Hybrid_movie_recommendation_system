import requests

API_KEY = "697a38cf7202936457b821fc7d019aea"

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def fetch_poster(movie_name):

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": API_KEY,
        "query": movie_name
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["results"]:

        poster_path = data["results"][0]["poster_path"]

        if poster_path:
            return IMAGE_URL + poster_path

    return None


def fetch_movie_details(movie_name):

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": API_KEY,
        "query": movie_name
    }

    response = requests.get(url, params=params)

    data = response.json()

    if not data["results"]:
        return None

    movie = data["results"][0]

    return {
        "title": movie.get("title"),
        "rating": movie.get("vote_average"),
        "overview": movie.get("overview"),
        "release_date": movie.get("release_date"),
        "poster": IMAGE_URL + movie["poster_path"]
        if movie.get("poster_path")
        else None
    }


if __name__ == "__main__":

    movie = "Avatar"

    print(fetch_poster(movie))

    print(fetch_movie_details(movie))