#buzzer

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def beep_buzz():
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4,True)
    time.sleep(0.5)
    GPIO.output(4,False)
    GPIO.cleanup(4)
    return;

#end of buzzer