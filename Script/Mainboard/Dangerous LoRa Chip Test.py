import adafruit_sdcard
import busio
import digitalio
import board
import storage
import microcontroller as mc
import time
# Connect to the card and mount the filesystem.
spi = busio.SPI(mc.pin.GPIO18, MOSI=board.MOSI0, MISO=board.MISO0)
cs = digitalio.DigitalInOut(mc.pin.GPIO17)
#cs.value = True
LoRa_ENABLE = digitalio.DigitalInOut(mc.pin.GPIO28)
LoRa_ENABLE.direction = digitalio.Direction.OUTPUT

RX_ENABLE = digitalio.DigitalInOut(mc.pin.GPIO20)
RX_ENABLE.direction = digitalio.Direction.OUTPUT

TX_ENABLE = digitalio.DigitalInOut(mc.pin.GPIO22)
TX_ENABLE.direction = digitalio.Direction.OUTPUT
LoRa_ENABLE.value = True

# Use the filesystem as normal.
while True:
   
    RX_ENABLE.value = False
    TX_ENABLE.value = True
    time.sleep(2)

    RX_ENABLE.value = True
    TX_ENABLE.value = False
    time.sleep(2)
