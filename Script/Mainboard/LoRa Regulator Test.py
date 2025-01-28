import adafruit_sdcard
import busio
import digitalio
import board
import storage
import microcontroller as mc
import time
ENABLE = digitalio.DigitalInOut(mc.pin.GPIO28)
ENABLE.direction = digitalio.Direction.OUTPUT

while True:
    ENABLE.value = True
    time.sleep(2)
    ENABLE.value = False
    time.sleep(2)
# Connect to the card and mount the filesystem.
#spi = busio.SPI(mc.pin.GPIO18, MOSI=board.MOSI0, MISO=board.MISO0)
#cs = digitalio.DigitalInOut(mc.pin.GPIO17)



