import requests
import random
from flask import Flask, render_template, jsonify
app = Flask(__name__)


while True:  
# this route only handle the rendering of index.html

    @app.route("/index.html")
    def main():
       return render_template('index.html')

    @app.route("/geomap.html")
    def maps():
       return render_template('geomap.html')

    @app.route("/homepage.html")
    def graphs():
       return render_template('homepage.html')

    @app.route("/BrPM")
    def BrPM():
        r = requests.get('http://192.168.11.2/BR') 
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200

    @app.route("/CoPM")
    def CrPM():
        r = requests.get('http://192.168.11.2/CR') 
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200

    @app.route("/Acc")
    def Acc():
        r = requests.get('http://192.168.11.2/Acc') 
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    
    @app.route("/RSSI")
    def RSSI():
        r = requests.get('http://192.168.11.2/RSSI') 
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    
    @app.route("/Alarm")
    def Alarm():
        r = requests.get('http://192.168.11.2/Alarm')
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    @app.route("/Gyro")
    def Gyro():
        r = requests.get('http://192.168.11.2/Gyro')
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    @app.route("/Temp")
    def Temp():
        r = requests.get('http://192.168.11.2/Temp')
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    @app.route("/HR")
    def HR():
        r = requests.get('http://192.168.11.2/HR')
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    @app.route("/SPO2")
    def SPO2():
        r = requests.get('http://192.168.11.2/SPO2')
        a = int(r.text)
        templateData = {'data' : a}
        return jsonify(templateData), 200
    @app.route("/lat")
    def lat():
        r = requests.get('http://192.168.11.2/lat')
        a = float(r.text)/1000000;
        templateData = {'data' : a}
        return jsonify(templateData), 200
    @app.route("/long")
    def long():
        r = requests.get('http://192.168.11.2/long')
        a = float(r.text)/1000000;
        print(a);
        templateData = {'data' : a}
        return jsonify(templateData), 200
# this route handling the request send to the /update uri
    
    if __name__ == "__main__":
        app.run()


