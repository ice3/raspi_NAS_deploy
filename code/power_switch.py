import time
import RPi.GPIO as GPIO

SWITCH_PORT = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PORT,  GPIO.IN, pull_up_down=GPIO.PUD_UP)


def my_callback(channel):
    print "falling edge detected on 17"

GPIO.add_event_detect(SWITCH_PORT, GPIO.FALLING,
                      callback=my_callback, bouncetime=300)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
