from microbit import *


# Start calibrating
# compass.calibrate()
# display.scroll('hello')
# Try to keep the needle pointed in (roughly) the correct direction
while True:
   sleep(100)
   h = compass.heading()
   needle = ((15 - h) // 30) % 12
   display.show(Image.ALL_CLOCKS[needle])
   print(h)
