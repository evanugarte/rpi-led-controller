from os import getenv, path, sep

CURRENT_DIR = path.dirname(path.abspath(__file__)) + sep


class SignMessage:
  def __init__(
      self,
      data,
      led_matrix_rows,
      led_matrix_columns,
      led_matrix_count,
      led_sign_directory=CURRENT_DIR
  ):
    self.scroll_speed = str(data.get("scrollSpeed", ""))
    self.background_color = data.get("backgroundColor", "")
    self.text_color = data.get("textColor", "")
    self.border_color = data.get("borderColor", "")
    self.text = data.get("text", "")
    self.brightness = str(data.get("brightness", 100))
    self.led_matrix_rows = led_matrix_rows
    self.led_matrix_columns = led_matrix_columns
    self.led_matrix_count = led_matrix_count
    self.led_sign_directory = led_sign_directory

  def hex_to_rgb(self, hex_value):
      return ",".join([str(int(hex_value[i:i+2], 16)) for i in (1, 3, 5)])

  def to_subprocess_command(self):
    led_matrix_count_flag = f"--led-chain={self.led_matrix_count}"
    led_matrix_rows_flag = f"--led-rows={self.led_matrix_rows}"
    led_matrix_columns_flag = f"--led-cols={self.led_matrix_columns}"
    return [
        self.led_sign_directory + "text-scroller",
        led_matrix_count_flag,
        led_matrix_rows_flag,
        led_matrix_columns_flag,
        "--led-gpio-mapping=adafruit-hat-pwm",
        "--led-slowdown-gpio=2",
        "-s", self.scroll_speed,
        "-B", self.hex_to_rgb(self.background_color),
        "-C", self.hex_to_rgb(self.text_color),
        "--led-brightness", self.brightness,
        "-O", self.hex_to_rgb(self.border_color),
        "-f", self.led_sign_directory + "10x20.bdf",
        "-y", "5",
        self.text
    ]

  def to_dict(self):
      return {
          "existingMessage": True,
          "scrollSpeed": self.scroll_speed,
          "backgroundColor": self.background_color,
          "textColor": self.text_color,
          "borderColor": self.border_color,
          "text": self.text,
          "success": True
      }
