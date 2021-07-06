import subprocess
from os import sep, path
from subprocess import call
import flask
from flask import Flask, request

proc = None
app = Flask(__name__)


def hex_to_rgb(hex_value):
    return ",".join([str(int(hex_value[i:i+2], 16)) for i in (0, 2, 4)])

@app.route("/api/health-check", methods=["GET"])
def health_check():
    return "Sign is up!" 

@app.route("/api/update-sign", methods=["POST", "GET"])
def hello_world():
    global proc
    postvars = request.json
    CURRENT_DIRECTORY = path.dirname(path.abspath(__file__)) + sep
    if proc != None:
        proc.kill()
    if len(postvars):
        command = [
            CURRENT_DIRECTORY + "text-scroller",
            "--led-rows=32",
            "--led-cols=64",
            "--led-chain=2",
            "--led-gpio-mapping=adafruit-hat-pwm",
            "--led-slowdown-gpio=2",
            # "--set-brightness", str(postvars["brightness"]),
            "-s", str(postvars["scrollSpeed"]),
            "-B", hex_to_rgb(postvars["backgroundColor"][1:]),
            "-C", hex_to_rgb(postvars["textColor"][1:]),
            "-O", hex_to_rgb(postvars["borderColor"][1:]),
            "-f", CURRENT_DIRECTORY + "10x20.bdf",
            postvars["text"],
        ]
        proc = subprocess.Popen(command)
    return "Hello, World!"

app.run(host="0.0.0.0", port=8080, debug=True, threaded=True)
