#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)  # channel=11 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            print dc
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
