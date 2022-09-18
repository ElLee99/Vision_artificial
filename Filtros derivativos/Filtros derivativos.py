# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:45:16 2022

@author: Johan Lee
"""

import cv2
import numpy as np


img = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Filtros derivativos/gt.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)


#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

#Laplaciano
img_lpc = cv2.Laplacian(img_gaussian, -1, ksize=3)


cv2.imshow("Original Image", img)
cv2.imshow("Black and white Image", gray)
cv2.imshow("Blurred Image", img_gaussian)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)
cv2.imshow("Laplace", img_lpc)

cv2.waitKey(0)
cv2.destroyAllWindows()