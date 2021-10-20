import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

servo_motor = 16
GPIO.setup(servo_motor, GPIO.OUT)
pulso = GPIO.PWM(servo_motor, 50)
pulso.start(2.5) #cero grados

try:
    while True:
        for i in range(0,180):
            grados = ((1.0/18.0)*i)+2.5
            pulso.ChangeDutyCycle(grados)
        sleep(2)
        for i in range(180,0,-1):
            grados = ((1.0/18.0)*i)+2.5
            pulso.ChangeDutyCycle(grados)
        sleep(2)
except KeyboardInterrupt:
    pulso.stop()
    GPIO.cleanup