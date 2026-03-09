from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_temmplate("index.html")  # serves templates/index.html
@app.route("/workout")
def workout():
    return render_temmplate("workout.html")  # serves templates/workout.html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
