import busio
import digitalio
import board
import storage
import microcontroller as mc
import time
# Connect to the card and mount the filesystem.
from adafruit_ds3231 import adafruit_ds3231



i2c = board.I2C()  # uses board.SCL and board.SDA
rtc = adafruit_ds3231.DS3231(i2c)
rtc.datetime = time.struct_time((2025,1,27,15,6,0,0,9,-1))

while True:
    t = rtc.datetime
    sleep(0.5)
    print(t)
    print(t.tm_hour, t.tm_min)

