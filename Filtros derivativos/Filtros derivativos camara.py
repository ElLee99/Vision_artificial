# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:27:16 2022

@author: Johan Lee
"""
import numpy as np
import cv2



def sketch (img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
    return img_gaussian
 

def sobelx (img):
    img_gaussian = sketch(img)
    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
    return img_sobelx


def sobely (img):
    img_gaussian = sketch(img)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
    return img_sobely


def sobelxy (img):
    img_sobelx = sobelx (img)
    img_sobely = sobely (img)
    img_sobel = img_sobelx + img_sobely
    return img_sobel


def prewittx (img):
    img_gaussian = sketch(img)
    
    kernelx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    return img_prewittx


def prewitty (img):
    img_gaussian = sketch(img)
    kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    return img_prewitty


def prewittxy (img):
    img_prewittx = prewittx (img)
    img_prewitty = prewitty (img)
    return img_prewittx + img_prewitty


def laplace (img):
    img_gaussian = sketch(img)
    img_lpc = cv2.Laplacian(img_gaussian, -1, ksize=3)
    return img_lpc


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("Video skecth", sketch(frame))
    cv2.imshow("Video sobelxy", sobelxy(frame))
    cv2.imshow("Video sobelx", sobelx(frame))
    cv2.imshow("Video sobely", sobely(frame))
    cv2.imshow("Video prewittx", prewittx(frame))
    cv2.imshow("Video prewitty", prewitty(frame))
    cv2.imshow("Video prewitt", prewittxy(frame))
    cv2.imshow("Video laplace", laplace(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()
