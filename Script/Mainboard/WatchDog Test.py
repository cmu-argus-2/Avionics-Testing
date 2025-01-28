import microcontroller as mc
import board
import digitalio
import time
import busio
print(mc.cpu.frequency) # read it to check
mc.cpu.frequency = 130000000
print(mc.cpu.frequency) # read it to check

pin8 = digitalio.DigitalInOut(mc.pin.GPIO6)
pin8.direction = digitalio.Direction.OUTPUT

while True:
   pin8.value = True
   time.sleep(0.3)
   pin8.value = False
   time.sleep(0.3)
   print("shiduo")
