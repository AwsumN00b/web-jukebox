from flask import Flask, request, render_template
import requests

app = Flask(__name__)
endpoint = "localhost:2112/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        songrequest = request.form.get("songname")
        
        requests.post(url=endpoint+"songrequest", data = {"song": songrequest})

        return songrequest + " has been added to the queue!"
    return render_template("index.html")


def main():
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
