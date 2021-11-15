## `server/` directory
The backend of this project. Takes requests from the frontend and uses an
 executable to write messages to the LED matrix.

### File Contents
- `10x20.bdf`: Font file used for sign messages
- `random.txt`: List containing random messages for the frontend. See the
 project's [README](https://github.com/evanugarte/rpi-led-controller/blob/master/README.md)
 for an example.
- `server.py`: Backend server. Accepts request from the frontend with flask.
- `sign_message.py`: Class for holding sign data
- `text-scroller`: Executable for writing to the LED Matrix. Compiled from
 @hzeller's rpi-rgb-led-matrix repository,
 [utils/text-scroller.cc](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/utils/text-scroller.cc)
