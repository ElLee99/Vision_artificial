# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:09:55 2022

@author: Johan Lee
"""


import cv2
import numpy as np

imgsp = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Filtros lineales/salypimienta.jfif")
graysp = cv2.cvtColor(imgsp, cv2.COLOR_BGR2GRAY)
imgguass = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Filtros lineales/ruidogaussiano.png")


imgfmedia= cv2.blur(graysp,(5,5)) #Filtro Media sal y pimienta
imgfgauss = cv2.GaussianBlur(graysp,(5,5),0) #Filtro Ruido Gaussiano sal y pimienta (img,kernel,desviacion estandar)
imgfmediagauss = cv2.blur(imgguass,(5,5))
imgfgaussruidogauss = cv2.GaussianBlur(imgguass,(5,5),0)


cv2.imshow("Imagen con rudio sal-pimienta",graysp)
cv2.imshow("Imagen con ruido gaussiano",imgguass)
cv2.imshow("Filtro Media de imagen con ruido sal-pimienta",imgfmedia)
cv2.imshow("Filtro Gaussiano de imagen con ruido sal-pimienta",imgfgauss)
cv2.imshow("Filtro Media de imagen con ruido gaussiano",imgfmediagauss)
cv2.imshow("Filtro Gaussiano de imagen con ruido gaussiano",imgfgaussruidogauss)


cv2.waitKey(0)
cv2.destroyAllWindows()