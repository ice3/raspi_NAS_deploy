#!/user/bin/env python

import time
import RPi.GPIO as gpio

PIN_LED = 24

gpio.setmode(gpio.BCM)
gpio.setup(PIN_LED, gpio.OUT)

try:
    while True:
        gpio.output(PIN_LED, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(PIN_LED, gpio.LOW)
        time.sleep(1.5)
except:
    gpio.cleanup()
