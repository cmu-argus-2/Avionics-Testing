import adafruit_sdcard
import busio
import digitalio
import board
import storage
import microcontroller as mc
# Connect to the card and mount the filesystem.
spi = busio.SPI(mc.pin.GPIO18, MOSI=board.MOSI0, MISO=board.MISO0)
cs = digitalio.DigitalInOut(mc.pin.GPIO26)
#cs.value = True

sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Use the filesystem as normal.
with open("/sd/test.txt", "w") as f:
    f.write("fhahfha\n")
with open("/sd/test.txt", "r") as f:
    readValue = f.read()
    print(readValue)
    