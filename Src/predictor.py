import os
import pickle
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "..", "Models")

model = pickle.load(
    open(
        os.path.join(
            MODEL_DIR,
            "popularity_model.pkl"
        ),
        "rb"
    )
)

def predict_popularity(
    vote_count,
    vote_average
):

    features = np.array([[
        vote_count,
        vote_average
    ]])

    prediction = model.predict(
        features
    )[0]

    return round(
        prediction,
        2
    )


if __name__ == "__main__":
    print(
        predict_popularity(
            1000,
            8.5
        )
    )