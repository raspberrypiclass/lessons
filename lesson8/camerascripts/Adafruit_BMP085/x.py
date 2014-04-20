from Adafruit_BMP085 import BMP085

bmp = BMP085(0x77)
temp = bmp.readTemperature()
print 'The temperature is %.1fC' %temp

