from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data (for demo purposes)
bus_status = {
    "bus_id": 1,
    "location": "Zarqa Main Station",
    "capacity": "Not Full"
}


@app.route("/")
def home():
    return jsonify({
        "system": "Smart University Shuttle Tracking",
        "status": "Running"
    })

@app.route("/bus/location", methods=["GET"])
def get_bus_location():
    return jsonify({
        "bus_id": bus_status["bus_id"],
        "location": bus_status["location"]
    })

@app.route("/bus/capacity", methods=["GET"])
def get_bus_capacity():
    return jsonify({
        "bus_id": bus_status["bus_id"],
        "capacity": bus_status["capacity"]
    })

@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.json
    return jsonify({
        "message": "Feedback received successfully",
        "feedback": data
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
