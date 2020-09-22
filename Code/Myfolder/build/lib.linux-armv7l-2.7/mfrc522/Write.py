#!usr/bin/env python
import RPi.GPIO as GPIO
import SimpleMFRC522

#GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522.SimpleMFRC522()

#text = ''

try:
    text=raw_input('Enter data:')
    print("Place Tag")
    reader.write(text)
    print("Successfull")
finally:
    GPIO.cleanup()

