import RPi.GPIO as GPIO
from time import sleep

pinL = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinL, GPIO.OUT)


GPIO.output(pinL, GPIO.HIGH)
sleep(5)
GPIO.output(pinL, GPIO.LOW)
sleep(4)

GPIO.output(pinL, GPIO.LOW)
GPIO.cleanup()