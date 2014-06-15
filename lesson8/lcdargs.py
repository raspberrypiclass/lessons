import sys

sys.path.append("/home/pi/lcd/quick2wire-python-api/")

from i2clibraries import i2c_lcd
from time import *

# Configuration parameters
# I2C Address, Port, Enable pin, RW pin, RS pin, Data 4 pin, Data 5 pin, Data 6$
lcd = i2c_lcd.i2c_lcd(0x27,1, 2, 1, 0, 4, 5, 6, 7, 3)

# If you want to disable the cursor, uncomment the following line
# lcd.command(lcd.CMD_Display_Control | lcd.OPT_Enable_Display)

lcd.backLightOn()

## read temp args
line1 = ''.join(sys.argv[1:])

lcd.setPosition(2, 0)
lcd.writeString(line1)
