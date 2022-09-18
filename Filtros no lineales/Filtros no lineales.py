# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:03:45 2022

@author: Johan Lee
"""

import cv2
import numpy as np

imgsp = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Filtros lineales/salypimienta.jfif")
graysp = cv2.cvtColor(imgsp, cv2.COLOR_BGR2GRAY)
imgguass = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Filtros lineales/ruidogaussiano.png")



imgfmediana = cv2.medianBlur(graysp, 3)
imgfmedianagauss = cv2.medianBlur(imgguass, 5)


kernel = np.ones((3,3), np.uint8)
imgmax = cv2.dilate(graysp, kernel)
imgmin = cv2.erode(graysp, kernel)


imgmaxgauss = cv2.dilate(imgguass, kernel)
imgmingauss = cv2.erode(imgguass, kernel)



cv2.imshow("Imagen con rudio sal-pimienta",graysp)
cv2.imshow("Imagen con ruido gaussiano",imgguass)
cv2.imshow("Filtro Mediana de imagen con ruido sal-pimienta",imgfmediana)
cv2.imshow("Filtro Minimo de imagen con ruido sal-pimienta",imgmin)
cv2.imshow("Filtro Maximo de imagen con ruido sal-pimienta",imgmax)
cv2.imshow("Filtro Mediana de imagen con ruido gaussiano",imgfmedianagauss)
cv2.imshow("Filtro Minimo de imagen con ruido gaussiano",imgmingauss)
cv2.imshow("Filtro Maximo de imagen con ruido gaussiano",imgmaxgauss)



cv2.waitKey(0)
cv2.destroyAllWindows()