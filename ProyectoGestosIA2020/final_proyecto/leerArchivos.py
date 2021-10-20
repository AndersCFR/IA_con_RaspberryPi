from os import scandir, getcwd
import cv2
import time
import sys

def ls(ruta=os(getcwd())):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]
fotos = ls('./fotos_demostracion')
print(type(fotos))
fotos.sort()
for i in fotos:
    print(i)
    #img = cv2.imread(str(i), cv2.COLOR_BGR2RGB)
    #cv2.imshow('Deteccion gestos',img)
    #cv2.waitKey(0)
    #time.sleep(3)
    #cv2.destroyAllWindows()