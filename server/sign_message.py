from os import sep, path

CURRENT_DIR = path.dirname(path.abspath(__file__)) + sep


class SignMessage:
  def __init__(self, data, led_sign_directory=CURRENT_DIR):
    self.led_sign_directory = led_sign_directory
    self.scroll_speed = str(data["scrollSpeed"])
    self.background_color = self.hex_to_rgb(data["backgroundColor"])
    self.text_color = self.hex_to_rgb(data["textColor"])
    self.border_color = self.hex_to_rgb(data["borderColor"])
    self.text = data["text"]

  def to_subprocess_command(self):
    return [
        self.led_sign_directory + "text-scroller",
        "--led-rows=32",
        "--led-cols=64",
        "--led-chain=2",
        "--led-gpio-mapping=adafruit-hat-pwm",
        "--led-slowdown-gpio=2",
        "-s", self.scroll_speed,
        "-B", self.background_color,
        "-C", self.text_color,
        "-O", self.border_color,
        "-f", self.led_sign_directory + "10x20.bdf",
        self.text
    ]

    def to_dict(self):
        return {
            "scrollSpeed": self.scroll_speed,
            "backgroundColor": self.background_color,
            "textColor": self.text_color,
            "borderColor": self.border_color,
            "text": self.text
        }

    def hex_to_rgb(self, hex_value):
        return ",".join([str(int(hex_value[i:i+2], 16)) for i in (0, 2, 4)])
