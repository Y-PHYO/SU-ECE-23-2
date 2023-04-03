# Turns halo light on and off

import RPi.GPIO as GPIO
import time


def lightOn():
     light1 = 21

     GPIO.setmode(GPIO.BCM)
     GPIO.setup(light1, GPIO.OUT)
     GPIO.output(light1, True)
     time.sleep(2)
     GPIO.setwarnings(False)
     GPIO.cleanup()

def lightOff():
     light1 = 21
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(light1, GPIO.OUT)
     GPIO.output(light1, False)
     time.sleep(2)
     GPIO.setwarnings(False)
     GPIO.cleanup()




