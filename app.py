from flask import Flask, request, render_template
import requests

app = Flask(__name__)
endpoint = "http://192.168.68.116:2112/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        songrequest = request.form.get("songname")
        print("HERE IT IS: ", songrequest)
        payload = {"song": songrequest}
        
        requests.post(url=endpoint+"songrequest", json=payload)

        return songrequest + " has been added to the queue!"
    return render_template("index.html")


def main():
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()
