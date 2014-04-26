#!/usr/bin/env python
import RPi.GPIO as GPIO

##tell the program which pin will be used to read the state of the button
pin = 12

## set pin numbering mode to board rather than chip
GPIO.setmode(GPIO.BOARD)
## tell the program we're going to be reading from the pin rather than outputting to it
GPIO.setup(pin,GPIO.IN)

##loop forever
##at each pass through the loop check the if the button has been pressed
##if it has output a message
while True:
	input_value = GPIO.input(pin)
	if GPIO.input(pin)== False:
		print("The button has been pressed.")
		while GPIO.input(pin) == False:
			pass
