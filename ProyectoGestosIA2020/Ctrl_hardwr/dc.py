
import RPi.GPIO as GPIO          
from time import sleep
import datetime
en = 22
in1 = 24
in2 = 26


GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
pulso=GPIO.PWM(en,1000)

pulso.start(100)   

def cont(max):
    n=0
    while n < max:
        yield n
        n = n+1

my_cont = cont(2000000)
for i in my_cont:
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
GPIO.setup(en,GPIO.LOW)
pulso.stop()
GPIO.cleanup()  