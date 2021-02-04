#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
from src.notifier import easy_sms

SignalPin = 18


def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
	GPIO.setup(SignalPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     # set SignalPin to 0V

def send_text(ev=None):
    easy_sms("Huxley go potty now")
    time.sleep(5)

def loop():
	GPIO.add_event_detect(SignalPin, GPIO.RISING, callback=send_text, bouncetime=5000) # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
	while True:
		time.sleep(1)   # Don't do anything

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

