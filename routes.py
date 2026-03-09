import csv
from flask import request, render_template
from datetime import date

file = "data/workouts.csv"


def log_workout():

    today = date.today()

    data = request.form

    with open(file, "a", newline="") as f:
        writer = csv.writer(f)

        for k in data:
            writer.writerow([today, k, data[k]])

    return "saved"
