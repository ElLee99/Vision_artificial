# -*- coding: utf-8 -*-

import numpy as np
import cv2

imgori=cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Coordenadas cromaticas/manooriginal.jpg")

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

minuni = np.empty((1, 3), int)
maxuni = np.empty((1, 3), int)
presuni = np.empty((1, 3), int)


for y in range(15):
    
    den = np.trunc((muestras[y, 0]) + (muestras[y, 1]) + (muestras[y,2]))
    presuni[0, 0] = np.trunc(muestras[y,0]/den*255)
    presuni[0, 1] = np.trunc(muestras[y, 1]/den*255)
    presuni[0, 2] = np.trunc(muestras[y, 2]/den*255)
        
    if y == 1:
        minuni[0, 0] = presuni[0, 0]
        maxuni[0, 0] = presuni[0, 0]
        minuni[0, 1] = presuni[0, 1]
        maxuni[0, 1] = presuni[0, 1]
        minuni[0, 2] = presuni[0, 2]
        maxuni[0, 2] = presuni[0, 2]
    
    else:
        if presuni[0, 0] < minuni[0, 0] :
            minuni[0, 0] = presuni[0, 0]
        if presuni[0, 0] > maxuni[0, 0] :
            maxuni[0, 0] = presuni[0, 0]
        if presuni[0, 1] < minuni[0, 1] :
            minuni[0, 1] = presuni[0, 1]
        if presuni[0, 1] > maxuni[0, 1] :
            maxuni[0, 1] = presuni[0, 1]
        if presuni[0, 2] < minuni[0, 2] :
            minuni[0, 2] = presuni[0, 2]
        if presuni[0, 2] > maxuni[0, 2] :
            maxuni[0, 2] = presuni[0, 2]


def oscurecer(imagen, oscurecimiento):
    
    dimension = imagen.shape
    imgoscurecida = np.empty((dimension), int)
    for x in range(dimension[0]): 
        for y in range (dimension[1]):
            imgoscurecida[x,y,0] = np.trunc(imagen[x,y,0]*oscurecimiento)
            imgoscurecida[x,y,1] = np.trunc(imagen[x,y,1]*oscurecimiento) 
            imgoscurecida[x,y,2] = np.trunc(imagen[x,y,2]*oscurecimiento) 
    imgoscurecida= np.uint8(imgoscurecida)      
    return imgoscurecida 


def cromatica(imagen):
    
    dimension = imagen.shape
    imgcromatica = np.empty((dimension), int)
    imagen = np.float64(imagen)
    
    for x in range(dimension[0]):
        for y in range (dimension[1]):
            den = np.round(np.float64((imagen[x,y,0]) + (imagen[x,y,1]) + (imagen[x,y,2])), 16)
           
            
            if den <= 0.0:
                imgcromatica[x,y,0] = 0
                imgcromatica[x,y,1] = 0
                imgcromatica[x,y,2] = 0
            
            else:
                imgcromatica[x,y,0]= np.trunc(imagen[x,y,0]/den*255)
                imgcromatica[x,y,1]= np.trunc(imagen[x,y,1]/den*255)
                imgcromatica[x,y,2]= np.trunc(imagen[x,y,2]/den*255)
                
            """if den >= 0.0:    
                r = np.trunc(imagen[x,y,0]/den*255)
                g = np.trunc(imagen[x,y,1]/den*255)
                b = np.trunc(imagen[x,y,2]/den*255)
                
                if r>=255 and g<=0 and b<=0:
                    imgcromatica[x,y,0] = 0
                    imgcromatica[x,y,1] = 0
                    imgcromatica[x,y,2] = 0
                    
                elif r<=0 and g>=255 and b<=0:
                    imgcromatica[x,y,0] = 0
                    imgcromatica[x,y,1] = 0
                    imgcromatica[x,y,2] = 0
                
                elif r<=0 and g<=0 and b>=255:
                    imgcromatica[x,y,0] = 0
                    imgcromatica[x,y,1] = 0
                    imgcromatica[x,y,2] = 0
                else:
                    imgcromatica[x,y,0]= r#np.trunc(imagen[x,y,0]/den*255)
                    imgcromatica[x,y,1]= g#np.trunc(imagen[x,y,1]/den*255)
                    imgcromatica[x,y,2]= b#np.trunc(imagen[x,y,2]/den*255)"""
        
    imgcromatica= np.uint8(imgcromatica)
    return imgcromatica


def blancoynegro(imagen):
    
    dimension = imagen.shape
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    imgbyn = np.empty((dimension), int)
    
    for x in range (dimension [0]):
        for y in range (dimension[1]):
            if imagen[x, y, 0] >= minuni[0, 0] and imagen[x, y, 0] <= maxuni [0, 0] and imagen[x, y, 1] >= minuni [0, 1] and imagen[x, y, 1] <= maxuni[0, 1] and imagen[x, y, 2] >= minuni[0, 2] and imagen[x, y, 2] <= maxuni[0, 2]:
                imgbyn[x,y] = 255
            else:
                imgbyn[x,y] = 0

    imgbyn= np.uint8(imgbyn)
    return imgbyn


#Resize Image Output for Windowed View
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    #Initialize the dimensions of the image to be resized and grab the image size
    dim = None
    (h, w) = image.shape[:2]
    #If both the width and height are None, then return the original image
    if width is None and height is None:
        return image
    #Check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    #Otherwise, the height is None
    else:
        #Calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    #Resize the image
    resized = cv2.resize(image, dim, interpolation = inter)
    #Return the resized image
    return resized


oscurecida1 = oscurecer(imgori, 0.8)
oscurecida2 = oscurecer(imgori, 0.4)

cromatica1 = cromatica(imgori)
cromatica2 = cromatica(oscurecida1)
cromatica3 = cromatica(oscurecida2)

byn1 = blancoynegro(cromatica1)
byn2 = blancoynegro(cromatica2)
byn3 = blancoynegro(cromatica3)


cv2.imshow('Imagen original', image_resize(imgori, height = 200))
cv2.moveWindow('Imagen original', 20, 0)
cv2.imshow('Imagen original cromatica', image_resize(cromatica1, height = 200))
cv2.moveWindow('Imagen original cromatica', 20, 240)
cv2.imshow('Imagen a blanco y negro de cromatica original', image_resize(byn1, height = 200))
cv2.moveWindow('Imagen a blanco y negro de cromatica original', 20, 480)

cv2.imshow('Imagen con brillo al 80%', image_resize(oscurecida1, height = 200))
cv2.moveWindow('Imagen con brillo al 80%', 400, 0)
cv2.imshow('Imagen cromatica con brillo al 80%', image_resize(cromatica2, height = 200))
cv2.moveWindow('Imagen cromatica con brillo al 80%', 400, 240)
cv2.imshow('Imagen a blanco y negro de cromatica con brillo al 80%', image_resize(byn2, height = 200))
cv2.moveWindow('Imagen a blanco y negro de cromatica con brillo al 80%', 400, 480)

cv2.imshow('Imagen con brillo al 40%', image_resize(oscurecida2, height = 200))
cv2.moveWindow('Imagen con brillo al 40%', 785, 0)
cv2.imshow('Imagen cromatica con brillo al 40%', image_resize(cromatica3, height = 200 ))
cv2.moveWindow('Imagen cromatica con brillo al 40%', 785, 240)
cv2.imshow('Imagen a blanco y negro de cromatica con brillo al 40%', image_resize(byn3, height = 200))
cv2.moveWindow('Imagen a blanco y negro de cromatica con brillo al 40%', 785, 480)


cv2.waitKey(0)
cv2.destroyAllWindows()  

