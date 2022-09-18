# -*- coding: utf-8 -*-


import numpy as np
import cv2

imgori = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/White patch/manolargafondogris.jpg")


def colorear(imagen, red, green, blue):
    
    dimension = imagen.shape
    imgcoloreada = np.empty((dimension), int)
    for x in range(dimension[0]): 
        for y in range (dimension[1]):
            val0 = np.trunc(imagen[x,y,0]*red)
            if val0 >= 255:
                imgcoloreada[x,y,0] = 255
            else:
                imgcoloreada[x,y,0] = val0
                
            val1 = np.trunc(imagen[x,y,1]*green) 
            if val1 >= 255:
                imgcoloreada[x,y,1] = 255
            else:
                imgcoloreada[x,y,1] = val1

            
            val2 = np.trunc(imagen[x,y,2]*blue) 
            if val2 >= 255:
                imgcoloreada[x,y,2] = 255
            else:
                imgcoloreada[x,y,2] = val2


    imgcoloreada = np.uint8(imgcoloreada)      
    return imgcoloreada






#BGR
maxirojo = [217, 224, 255] # mano sobre fondo gris
maxiazul = [249, 215, 240]
maxiverde = [206, 254, 236]
maxiori = [210, 219, 241]


def whitepatch(imagen, color):
    
    dimension = imagen.shape
    imgwp = np.empty((dimension), int)
    imagen = np.float64(imagen)
    
    if  color == 'original':    
        maxi = maxiori
        print("es original")
    
    
    if  color == 'rojo':    
        maxi = maxirojo
        print("es rojo")
        
    if  color == 'verde':    
        maxi = maxiverde
        print("es verde")
    
    if  color == 'azul':    
        maxi = maxiazul
        print("es azul")
        
    print(maxi[0], maxi[1], maxi[2])
        
    
    for x in range(dimension[0]):
        for y in range (dimension[1]):
           
                
            if np.trunc(imagen[x,y,0]/maxi[0]*255) >= 255:
                imgwp[x,y,0] = 255
            else:
                imgwp[x,y,0]= np.trunc(imagen[x,y,0]/maxi[0]*255)
              
            if np.trunc(imagen[x,y,1]/maxi[1]*255) >= 255:
                imgwp[x,y,1] = 255
            else:
                imgwp[x,y,1]= np.trunc(imagen[x,y,1]/maxi[1]*255)
            
            if np.trunc(imagen[x,y,2]/maxi[2]*255) >= 255:
                imgwp[x,y,2] = 255
            else:
                imgwp[x,y,2]= np.trunc(imagen[x,y,2]/maxi[2]*255)
        
    imgwp= np.uint8(imgwp)
    return imgwp


def blancoynegro(imagen):
    
    maxbyn = [185, 192, 201]
    minbyn = [102, 109, 115]

    
    dimension = imagen.shape
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    imgbyn = np.empty((dimension), int)
    
    for x in range (dimension [0]):
        for y in range (dimension[1]):
            if imagen[x, y, 0] >= minbyn[0] and imagen[x, y, 0] <= maxbyn [0] and imagen[x, y, 1] >= minbyn [1] and imagen[x, y, 1] <= maxbyn[1] and imagen[x, y, 2] >= minbyn[2] and imagen[x, y, 2] <= maxbyn[2]:
                imgbyn[x,y] = 0
            else:
                imgbyn[x,y] = 255

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



imgroja = colorear(imgori, 1, 1, 1.2)
imgverde = colorear(imgori, 1, 1.2, 1)
imgazul = colorear(imgori, 1.2, 1, 1)

originalwp = whitepatch(imgori, 'original')
rojowp = whitepatch(imgroja, 'rojo')
verdewp = whitepatch(imgverde, 'verde')
azulwp = whitepatch(imgazul, 'azul')


bynwpori = blancoynegro(originalwp)
bynwprojo = blancoynegro(rojowp)
bynwpverde = blancoynegro(verdewp)
bynwpazul = blancoynegro(azulwp)



cv2.imshow('Imagen original', image_resize(imgori, height = 200))
cv2.moveWindow('Imagen original', 20, 20)
cv2.imshow('Imagen original white patch', image_resize(originalwp, height = 200))
cv2.moveWindow('Imagen original white patch', 20, 240)
cv2.imshow('Imagen original white patch a byn',image_resize(bynwpori, height = 200))
cv2.moveWindow('Imagen original white patch a byn', 20, 480)


cv2.imshow('Imagen roja', image_resize(imgroja, height = 200))
cv2.moveWindow('Imagen roja', 400, 20)
cv2.imshow('Imagen roja white patch', image_resize(rojowp, height = 200))
cv2.moveWindow('Imagen roja white patch', 400, 240)
cv2.imshow('Imagen roja white patch a byn', image_resize(bynwprojo, height = 200))
cv2.moveWindow('Imagen roja white patch a byn', 400, 480)


cv2.imshow('Imagen verde', image_resize(imgverde, height = 200))
cv2.moveWindow('Imagen verde', 785, 20)
cv2.imshow('Imagen verde white patch', image_resize(verdewp, height = 200))
cv2.moveWindow('Imagen verde white patch', 785, 240)
cv2.imshow('Imagen verde white patch a byn', image_resize(bynwpverde, height = 200))
cv2.moveWindow('Imagen verde white patch a byn', 785, 480)



cv2.imshow('Imagen azul', image_resize(imgazul, height = 200))
cv2.imshow('Imagen azul white patch', image_resize(azulwp, height = 200))
cv2.imshow('Imagen azul white patch a byn', image_resize(bynwpazul, height =200))


cv2.waitKey(0)
cv2.destroyAllWindows()  