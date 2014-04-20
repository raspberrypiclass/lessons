import picamera
import sys
import os
import time

if not len(sys.argv) > 1:
	sys.exit('You need to enter a filename')
filename = sys.argv[1]
#try:
#	overlay = sys.argv[2]
#except:
#	pass

with picamera.PiCamera() as camera:
	camera.start_preview()
	time.sleep(2)
	camera.capture(filename)
	camera.stop_preview() 
overlay = raw_input('Enter the text to overlay')
cmdline = 'sudo convert %s -pointsize 36 -fill white -annotate +40+141 "%s" %s' %(filename,overlay,filename)
if overlay:
	print cmdline
	os.system(cmdline)

