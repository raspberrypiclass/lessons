import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

value = ''

while value != 'off' and  value != 'on':
	value = raw_input('Off or on?').lower()

	if value == 'off':
		GPIO.output(11,False)
	elif value == 'on':
		GPIO.output(11,True)
	else:
		print 'Tell me off or on'


