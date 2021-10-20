import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinR = 8
GPIO.setup(pinR, GPIO.OUT)
pinG = 10
GPIO.setup(pinG, GPIO.OUT)
pinB = 12
GPIO.setup(pinB, GPIO.OUT)

for i in range(0,8):
    GPIO.output(pinR, GPIO.HIGH)
    GPIO.output(pinG, GPIO.LOW)
    GPIO.output(pinB, GPIO.LOW)
    time.sleep(2)
    GPIO.output(pinR, GPIO.LOW)
    GPIO.output(pinG, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)
    time.sleep(2)
    GPIO.output(pinR, GPIO.LOW)
    GPIO.output(pinG, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    time.sleep(2)

GPIO.cleanup()