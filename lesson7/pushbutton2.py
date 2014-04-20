#!/usr/bin/env python
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

pushcount = 0

while True:
	input_value = GPIO.input(12)
	if GPIO.input(12)== False:
		print("The button has been pressed.")
		pushcount += 1
		os.system('ls -l')
		while GPIO.input(12) == False:
			pass
os.system('cat %d %s >> /var/www/pushbutton.html') % (pushcount,'<br><br>')

