import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

p = GPIO.PWM(11,0.5)
p.start(10)
raw_input('Press return to stop')
p.stop()
GPIO.cleanup()

