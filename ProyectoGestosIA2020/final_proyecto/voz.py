from gtts import gTTS
import pyttsx3
import os
from time import sleep
#engine = pyttsx3.init()
#engine.say('Hola amigo como te encuentras este dia')
#engine.runAndWait()

o = gTTS(text='Se ha detectado gesto de mano abierta se encendera la luz',lang='es')
o.save("1.mp3")
o1 = gTTS(text='se ha detectado gesto de mano cerrado se encendera el ventilado',lang='es')
o1.save("2.mp3")
o2 = gTTS(text='se ha detectado gesto de dos dedos se abrira el garage',lang='es')
o2.save("3.mp3")

os.system("vlc 1.mp3")

os.system("vlc 2.mp3")

os.system("pkill vlc")