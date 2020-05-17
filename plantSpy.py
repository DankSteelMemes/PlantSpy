import board
import neopixel
import time
from datetime import datetime
import os, sys

led_count = 8
led_pin = board.D18
led_brightness = 0.4
led_order = neopixel.RGB

daylight = False

strip = neopixel.NeoPixel(led_pin, led_count)

def lights_on():
	strip[0] = (235,240,230)
	strip[1] = (239,242,225)
	strip[2] = (243,245,220)
	strip[3] = (247,247,215)
	strip[4] = (247,247,215)
	strip[5] = (243,245,220)
	strip[6] = (239,242,225)
	strip[7] = (235,240,230)


def lights_off():
        strip.fill((0,0,0))

while True:
	try:
		now = datetime.now()
		if now.hour > 7 and now.hour < 19:
			lights_on()
			daylight = True
		else:
			daylight = False
		dt_string = now.strftime("%b-%d-%Y__%H-%M") + ".jpg"
		os.system('fswebcam -r 1280x960 -D 3 --no-banner /home/pi/growingPlantPictures/webcam/{}'.format(dt_string))
		time.sleep(3)
		if daylight:
			lights_off()
	except Exception as e:
		print(e)
	finally:
		time.sleep(1800) #3600 is 1 hour
