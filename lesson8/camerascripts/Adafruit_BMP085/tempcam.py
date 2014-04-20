import picamera
import sys
import os
import time
from Adafruit_BMP085 import BMP085

if not len(sys.argv) > 1:
	sys.exit('You need to enter a filename')
filename = sys.argv[1]

bmp = BMP085(0x77)
temp = bmp.readTemperature()

with picamera.PiCamera() as camera:
	camera.start_preview()
	time.sleep(2)
	camera.capture(filename)
	camera.stop_preview() 
overlay = "Temperature: %.2f C" % temp
cmdline = 'sudo convert %s -pointsize 36 -fill white -annotate +40+141 "%s" %s' %(filename,overlay,filename)
if overlay:
	print cmdline
	os.system(cmdline)

