import time
import RPi.GPIO as GPIO
import os

SWITCH_PORT = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PORT,  GPIO.IN, pull_up_down=GPIO.PUD_UP)


def shutdown_callback(channel):
    print "shutting down"
    os.system('sudo poweroff')

GPIO.add_event_detect(SWITCH_PORT, GPIO.FALLING,
                      callback=my_callback, bouncetime=300)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
