# Turns halo light on and off
light1 = 21
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(light1, GPIO.OUT)
while True:
     GPIO.output(light1, True)
     time.sleep(2)
     GPIO.output(light1, False)
     time.sleep(2)
    
    
GPIO.setwarnings(False)  
GPIO.cleanup()
