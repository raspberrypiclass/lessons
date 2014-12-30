import wiringpi2 as wp
import time

PWM_MODE_MS = 0
PWM_PIN = 12

def main():

  # use BCM GPIO numbers
  wp.wiringPiSetupPhys()
  # enable PWM0
  wp.pinMode(12,2)
  # switch from default mode to mark:space mode
  wp.pwmSetMode(PWM_MODE_MS)
  wp.pwmSetClock(200)
  wp.pwmWrite(12, 0)

  while True:
    try:
  wp.pwmWrite(12, 2)
      time.sleep(3)
      # turn then wait
      wp.pwmWrite(12,128)
      time.sleep(3)
      # turn then wait
      wp.pwmWrite(12, 256)
      time.sleep(3)
    except Exception,e:
      print str(e)
      # clean up
      wp.pwmWrite(12, 0)
      print("exiting.")
      break

  if __name__ == '__main__':
      main()
