from microbit import *

DEFAULT_PERIOD = 100
MIN_PERIOD = 20
MAX_PERIOD = 2500
PERIOD_FACTOR = 5

# Get dummy compass measurement, to trigger calibration if necessary
dummy = compass.heading()
period = DEFAULT_PERIOD
display.show(Image.HEART)

def reset():
  global next_time, seq
  next_time = running_time();
  seq = 0

def change_period(p):
  global period, MIN_PERIOD, MAX_PERIOD
  if p >= MIN_PERIOD and p <= MAX_PERIOD:
    period = p
    reset()

reset()

while True:
   heading = compass.heading()
   accel =  accelerometer.get_values()
   temp = temperature()
   curr_time = running_time()
   if curr_time >= next_time:
     seq = seq + 1
     print("%s,%s,%s,%s,%s,%s,%s" % 
        (seq, curr_time, heading, accel[0], accel[1], accel[2], temp))
     next_time = next_time + period
     display.set_pixel(2, 2, seq % 10)
   else: 
    sleep(1)
    if button_a.was_pressed():
      change_period(period * PERIOD_FACTOR) 
    elif button_b.was_pressed():
      change_period(period / PERIOD_FACTOR) 
