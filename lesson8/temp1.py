#!/usr/bin/python

from Adafruit_BMP085 import BMP085

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

temp = bmp.readTemperature()

print "Temperature: %.2f C" % temp
