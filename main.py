from machine import Pin
from neopixel import NeoPixel
import time

touch = Pin(15, Pin.IN)   # OUT pin from sensor
pin = Pin(16)
led = NeoPixel(pin, 1)    # Onboard NeoPixel

led_state = False
auto_off_delay = 60   # seconds before auto shut-off
last_on_time = 0

while True:
    if touch.value() == 1:
        led_state = not led_state
        if led_state:
            led[0]=(0,255,255)
            last_on_time = time.time()
        else:
            led[0]=(0,0,0)
        led.write()
        while touch.value() == 1:
            time.sleep(0.05)

    if led_state and (time.time() - last_on_time >= auto_off_delay):
        led_state = False
        led[0]=(0,0,0)
        led.write()

    time.sleep(0.1)
