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

while True:
    t = rtc.datetime
    sleep(0.5)
    print(t)
    print(t.tm_hour, t.tm_min)