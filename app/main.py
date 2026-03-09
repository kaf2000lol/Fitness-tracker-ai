from flask import Flask, render_template

app = Flask(__name__, temmplate_folder="temmplate")  # <-- your folder name

@app.route("/")
def home():
    return render_temmplate("index.html")  # serves index.html

@app.route("/workout")
def workout():
    return render_temmplate("workout.html")  # serves workout.html

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
