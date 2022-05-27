from flask import Flask, jsonify
from flask_cors import CORS
import os

from temphum import temphum

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

isOn = False

@app.route("/onoff", methods=["GET"])
def hello_world():
  global isOn
  if isOn:
    os.system("irsend SEND_ONCE aircon SWITCH_OFF")
    isOn = False
  else:
    os.system("irsend SEND_ONCE aircon SWITCH_ON")
    isOn = True
  response = jsonify({"status": "200"})
  return response

@app.route("/refresh", methods=["GET"])
def refresh():
  temp, hum = temphum()
  if temp is not None and hum is not None:
    response = jsonify({ "status": "200", 
                         "temperature": f"{temp}°C", 
                         "humidity": f"{hum}%" })
    return response
  else:
    response = jsonify({ "status": "500" })

if __name__=="__main__":
  app.run(host='0.0.0.0')