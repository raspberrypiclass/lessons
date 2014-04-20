#! /usr/bin/env python
from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

count = int(raw_input("How many times would you like to blink the led?"))

while count > 0:
	GPIO.output(12, True)
	sleep(1)
	GPIO.output(12, False)
	sleep(1)
	count = count - 1
