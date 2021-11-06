# rpi-led-controller
Controlling an LED matrix from a website hosted on a raspberry pi

## Prerequisites:
- 2 [64x32 RGB LED Matrix](https://www.adafruit.com/product/2279)
- [Adafruit RGB Matrix Bonnet for Raspberry Pi](https://www.adafruit.com/product/3211)
- Any normal size raspberry pi (so that the bonnet can fit on top of it)

## Running the website
1. Boot your Pi with raspbian and with a network connection
2. Follow the wiring guide from @hzeller ([link](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md))
3. Install docker and docker-compose
4. Run the website with:
```
sudo docker-compose up
```
**Note:** we use sudo to give docker access to the pi's GPIO pins.

5. After some time, the website should appear, accessible from port 80 on the pi:
![image](https://user-images.githubusercontent.com/36345325/140591851-08f9b5b5-c92d-4286-a5c8-60ceb5c45ba1.png)

The random button yields a random phrase and colors to test the sign:

![image](https://user-images.githubusercontent.com/36345325/140591859-227baa9f-444c-48dd-9f44-b7b50376346e.png)
