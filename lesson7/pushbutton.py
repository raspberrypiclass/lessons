import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

while True:
	input_value = GPIO.input(12)
	if GPIO.input(12)== False:
		print("The button has been pressed.")
		while GPIO.input(12) == False:
			pass
