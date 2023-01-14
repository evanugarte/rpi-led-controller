import argparse
from os import sep, path
import random
import subprocess

from sign_message import SignMessage

from flask import Flask, request, jsonify

parser = argparse.ArgumentParser()
parser.add_argument(
    "--host",
    default="0.0.0.0",
    help="The network interface for the server to listen on. Default is 0.0.0.0",
)
parser.add_argument(
    "--port",
    help="The port for the server to listen on.",
    required=True,
    type=int,
)
parser.add_argument(
    "--led_matrix_rows",
    help="The number of rows in the LED matrix attached to the Pi. See the README for more information.",
    required=True,
)
parser.add_argument(
    "--led_matrix_columns",
    help="The number of columns in an LED matrix attached to the Pi. See the README for more information.",
    required=True,
)
parser.add_argument(
    "--led_matrix_count",
    help="The number of LED matrices daisy chained together. See the README for more information.",
    required=True,
)
args = parser.parse_args()

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


@app.route("/api/random", methods=["GET"])
def random_message():
    text = subprocess.check_output(
        "sort -R random.txt | head -n1",
        shell=True).decode('utf-8').strip().replace("\\", "")
    text_color = "#%06x" % random.randint(0, 0xFFFFFF)
    background_color = "#%06x" % random.randint(0, 0xFFFFFF)
    border_color = "#%06x" % random.randint(0, 0xFFFFFF)
    return jsonify({
        "scrollSpeed": 10,
        "backgroundColor": background_color,
        "textColor": text_color,
        "borderColor": border_color,
        "text": text,
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
            sign_message = SignMessage(
                data,
                args.led_matrix_rows,
                args.led_matrix_columns,
                args.led_matrix_count,
            )
            proc = subprocess.Popen(sign_message.to_subprocess_command())
        success = True
        return jsonify({
            "success": success
        })
    except:
        sign_message = None
        return "Could not update sign", 500


if __name__ == "__main__":
    app.run(host=args.host, port=args.port, debug=True, threaded=True)
