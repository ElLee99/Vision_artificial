# -*- coding: utf-8 -*-

import numpy as np
import cv2

imagenori2=cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Descriptor simple/manooriginal.jpg")
imagenori= cv2.cvtColor(imagenori2,cv2.COLOR_BGR2RGB)
dimension = imagenori.shape
imagen2 = np.empty((dimension), int)

muestras = np.array([
 [184, 115, 83],
 [249, 210, 169],
 [211, 115, 87],
 [249, 209, 157],
 [157, 98, 64],
 [204, 105, 64],
 [244, 172, 134],
 [246, 150, 105],
 [253, 201, 148],
 [255, 174, 128],
 [243, 200, 165],
 [252, 207, 150],
 [252, 211, 159],
 [253, 212, 160],
 [253, 213, 161],
 [252, 215, 162],
])

mini = [157, 98, 64]
maxi = [255, 215, 169]

for x in range (dimension [0]):
    for y in range (dimension[1]):
        if imagenori[x, y, 0] >= mini[0] and imagenori[x, y, 0] <= maxi [0] and imagenori[x, y, 1] >= mini [1] and imagenori[x, y, 1] <= maxi[1] and imagenori[x, y, 2] >= mini [2] and imagenori[x, y, 2] <= maxi[2]:
            imagen2[x,y] = 255
        else:
            imagen2[x,y] = 0


mininp= np.array(mini) 
maxinp= np.array(maxi) 
mask = cv2.inRange(imagenori, mininp, maxinp)
contorno, jerarquia= cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE )
imagen2= np.uint8(imagen2)


if len(contorno)!=0:
    for contorno in contorno:
        if cv2.contourArea(contorno)>500:
            x,y,w,h =cv2.boundingRect(contorno)
            cv2.rectangle(imagen2, (x,y), (x+w , y+h), (255, 0, 0),2)


cv2.imshow('Imagen original', imagenori2)
cv2.imshow('Imagen descrita', imagen2)
cv2.waitKey(0)
cv2.destroyAllWindows()    