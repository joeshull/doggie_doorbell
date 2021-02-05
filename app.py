#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
from src.notifier import easy_sms

SignalPin = 18


def setup():
	GPIO.setmode(GPIO.BCM)       # BCM order for GPIO pins
	GPIO.setup(SignalPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     # set SignalPin to 0V

def send_text(ev=None):
    easy_sms("Huxley go potty now")

def loop():
        GPIO.add_event_detect(SignalPin, GPIO.RISING, callback=send_text, bouncetime=10000) # wait for rising voltage and set bouncetime to mitigate multiple texts
        while True:
            time.sleep(5) # Don't do anything

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
