from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Your API URL and Key
url = "https://api.x.ai/v1/chat/completions"
api_key = "<API-key>"  # enter your api key here


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["prompt"]

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    data = {
        "messages": [
            {"role": "system", "content": "You are a test assistant."},
            {"role": "user", "content": user_input},
        ],
        "model": "grok-beta",
        "stream": False,
        "temperature": 0,
    }

    # Make the POST request to the API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # If the response is valid, return the content as JSON
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to get a response from the API."})


if __name__ == "__main__":
    app.run(debug=True)
