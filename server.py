from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

events = [
    {"id": 1, "title": "Community Meetup"},
    {"id": 2, "title": "Tech Conference"},
]

@app.get("/")
def home():
    return jsonify({"message": "Welcome to the event catalog!"})

@app.get("/events")
def get_events():
    return jsonify(events)

@app.post("/events")
def create_event():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object with a title is required."}), 400

    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required."}), 400

    event = {
        "id": max((item["id"] for item in events if isinstance(item.get("id"), int)), default=0) + 1,
        "title": title,
    }
    events.append(event)
    return jsonify(event), 201

if __name__ == "__main__":
    app.run(debug=True)
