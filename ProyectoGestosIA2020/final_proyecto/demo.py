import numpy as np
import time
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import os
import sys
import cv2
import RPi.GPIO as GPIO
from time import sleep
import datetime


def ls(ruta=os.getcwd()):
    return [arch.name for arch in os.scandir(ruta) if arch.is_file()]

class servoMotor:
    def mover():
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

class dcMotor:
    def girar():
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

        my_cont = cont(4000000)
        for i in my_cont:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
        GPIO.setup(en,GPIO.LOW)
        pulso.stop()
        GPIO.cleanup()
        
class led():
    def encender():
        pinL = 18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pinL, GPIO.OUT)

        GPIO.output(pinL, GPIO.HIGH)
        sleep(5)
        GPIO.output(pinL, GPIO.LOW)
        sleep(4)

        GPIO.output(pinL, GPIO.LOW)
        GPIO.cleanup()
        
dc = dcMotor
luz = led
servo = servoMotor




modelo_entrenado = './modelo/modelo.h5'
pesos = './modelo/pesos.h5'
cnn = load_model(modelo_entrenado)
cnn.load_weights(pesos)
dsize = (100,100)


def predict(file):
    flag = False
    x=load_img(file, target_size=(100, 100))
    x=img_to_array(x)
    x=np.expand_dims(x,axis=0)
    arreglo = cnn.predict(x) #[1,0,0]

    resultado=arreglo[0]

    for i in range(0,3):
        if resultado[i]>0.7:
            flag=True

    if flag==True:
        respuesta = np.argmax(resultado)
        if respuesta==0:
            print("Papel")
            os.system("vlc 1.mp3")
            luz.encender()
        elif respuesta == 1:
            print("Roca")
            os.system("vlc 2.mp3")       
            dc.girar()
        elif respuesta == 2:
            print("Tijera")
            os.system("vlc 3.mp3")
            servo.mover()
    else:
        respuesta=3
        print("Nada")
    #return respuesta


#predict('fotos_demostracion/papa3.jpeg')


fotos = ls('./fotos_demostracion')
print(type(fotos))
fotos.sort()
for i in fotos:
    os.system(str("fim -a "+str('./fotos_demostracion/'+i)))
    predict(str('./fotos_demostracion/'+i))
