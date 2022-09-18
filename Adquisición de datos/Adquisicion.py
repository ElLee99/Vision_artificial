# -*- coding: utf-8 -*-

import cv2

imagen=cv2.imread("c:/Users/Johan Lee/Desktop/Burguer.png")
cv2.imwrite('Hamburguesa2.0.jpg', imagen)
cv2.imshow('Prueba', imagen)
cv2.waitKey(0)
cv2.imwrite("c:/Users/Johan Lee/Desktop/Hamburguesa2.0.jpg", imagen)


leerVideo = cv2.VideoCapture("c:/Users/Johan Lee/Desktop/Taylorswift.mp4")
guardarVideo=cv2.VideoWriter('c:/Users/Johan Lee/Desktop/TS.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30.0, (854, 480))
while(leerVideo.isOpened()):
    ret, img=leerVideo.read()
    if ret==True:
        cv2.imshow('video', img)
        guardarVideo.write(img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        
        
leerVideo.release()
guardarVideo.release()
cv2.destroyAllWindows()
