
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

pinR = 8
GPIO.setup(pinR, GPIO.OUT)
pinG = 10
GPIO.setup(pinG, GPIO.OUT)
pinB = 12
GPIO.setup(pinB, GPIO.OUT)


servo_motor = 16
GPIO.setup(servo_motor, GPIO.OUT)
pulso = GPIO.PWM(servo_motor, 50)
pulso.start(2.5) #cero grados


for i in range(0,2):
    for i in range(0,180):
        GPIO.output(pinR, GPIO.LOW)
        GPIO.output(pinG, GPIO.HIGH)
        GPIO.output(pinB, GPIO.LOW)
        grados = ((1.0/18.0)*i)+2.5
        pulso.ChangeDutyCycle(grados)

    sleep(2)
    for i in range(180,0,-1):
        GPIO.output(pinR, GPIO.LOW)
        GPIO.output(pinG, GPIO.LOW)
        GPIO.output(pinB, GPIO.HIGH)
        grados = ((1.0/18.0)*i)+2.5
        pulso.ChangeDutyCycle(grados)
    sleep(2)
GPIO.setup(servo_motor,GPIO.LOW)
pulso.stop()
GPIO.cleanup
