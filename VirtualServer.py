import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/GPGGS")
def lat():
    # process the data using Python code
    name="GPS-tracer"
    id = 00000
    latitude = random.uniform(33.565111, 33.565200)
    longitude = random.uniform(73.016500, 73.016913)
    altitude = 0.00
    velocity=0.00
    gps_string = {"name": name, "id": id, "latitude": latitude, "longitude": longitude, "altitude": altitude,
                  "velocity": velocity}
    response = jsonify(gps_string)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090, debug=True)