import subprocess
from os import sep, path
from subprocess import call
import flask
from flask import Flask, request, jsonify

from sign_message import SignMessage

proc = None
sign_message = None
app = Flask(__name__)


def hex_to_rgb(hex_value):
    return ",".join([str(int(hex_value[i:i+2], 16)) for i in (0, 2, 4)])

@app.route("/api/health-check", methods=["GET"])
def health_check():
    global sign_message
    if sign_message:
        return jsonify(sign_message.to_dict())
    else:
        return jsonify({
            "success": True
        })

@app.route("/api/turn-off", methods=["GET"])
def turn_off():
    global proc
    global sign_message
    success = False
    if proc != None:
        proc.kill()
        sign_message = None
        success = True
    return jsonify({
        "success": success
    })

@app.route("/api/update-sign", methods=["POST"])
def update_sign():
    global proc
    global sign_message
    data = request.json
    CURRENT_DIRECTORY = path.dirname(path.abspath(__file__)) + sep
    success = False
    if proc != None:
        proc.kill()
    try:
        if data and len(data):
            sign_message = SignMessage(data)
            proc = subprocess.Popen(sign_message.to_subprocess_command())
        success = True
        return jsonify({
            "success": success
        })
    except:
        sign_message = None
        return "Could not update sign", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
