#!/usr/bin/env python
from RPi import GPIO
from time import sleep

#tell the program what pin is connected to the breadboard
pin = 11

##disable warnings
GPIO.setwarnings(False)

#set the numbering system
#BOARD = numbered by how the pins are laid out on the board
#BCM = numbered by the broadcom GPIO numbers
GPIO.setmode(GPIO.BOARD)

##set the pin to output state rather than input
##this uses the variable defined at the start of the code
GPIO.setup(pin, GPIO.OUT)

## ask the user for a number to decide how many times to loop
count = int(raw_input("How many times would you like to blink the led?"))

##loop the number of times the user has asked us to
## within the loop the pin output is switched to high (led is on)
## then we pause by calling the sleep function
## then we set output to low (led is off)
##This makes the led blink
while count > 0:
	GPIO.output(pin, True)
	sleep(1)
	GPIO.output(pin, False)
	sleep(1)
	count = count - 1
