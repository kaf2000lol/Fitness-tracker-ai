import pandas as pd
import matplotlib.pyplot as plt

def make_graph():

    df = pd.read_csv("data/workouts.csv")

    squat = df[df["exercise"] == "squat"]

    plt.plot(squat["date"], squat["weight"])

    plt.savefig("graphs/squat.png")
