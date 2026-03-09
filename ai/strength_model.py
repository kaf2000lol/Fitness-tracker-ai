import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


def predict_next(exercise):

    df = pd.read_csv("data/workouts.csv")

    ex = df[df["exercise"] == exercise]

    x = np.arange(len(ex)).reshape(-1, 1)
    y = ex["weight"]

    model = LinearRegression()
    model.fit(x, y)

    next_x = [[len(ex)]]

    return model.predict(next_x)[0]
