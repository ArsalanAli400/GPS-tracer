import requests
import random
from flask import Flask, render_template, jsonify
app = Flask(__name__)


while True:  
# this route only handle the rendering of index.html

    # @app.route("/index.html")
    # def main():
    #    return render_template('index.html')

    @app.route("/lat")
    def lat():
        lat = random.uniform(33.565111, 33.565200)
        templateData = {'data': lat}
        return jsonify(templateData), 200

    @app.route("/long")
    def long():
        long = random.uniform(73.016500, 73.016913)
        templateData = {'data' : long}
        return jsonify(templateData), 200
# this route handling the request send to the /update uri
    
    if __name__ == "__main__":
        app.run()


