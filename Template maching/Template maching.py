# -*- coding: utf-8 -*-

import numpy as np
import cv2

imgori = cv2.imread("C:/Users/Johan Lee/Documents/Ing Mecatronica/6to/Vision artificial/Template maching/manos.jpg")



def blancoynegro(imagen):
    
   
    
    maxbyn = [255, 230, 255]
    minbyn = [5, 5, 5]

    
    dimension = imagen.shape
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    imgbyn = np.empty((dimension), int)
    
    for x in range (dimension [0]):
        for y in range (dimension[1]):
            if imagen[x, y, 0] >= minbyn[0] and imagen[x, y, 0] <= maxbyn [0] and imagen[x, y, 1] >= minbyn [1] and imagen[x, y, 1] <= maxbyn[1] and imagen[x, y, 2] >= minbyn[2] and imagen[x, y, 2] <= maxbyn[2]:
                imgbyn[x,y] = 255
            else:
                imgbyn[x,y] = 0

    imgbyn= np.uint8(imgbyn)
    return imgbyn



def etiquetas (imagen):
    
    dimension = imagen.shape
    print(dimension)
    imgetiquetada = np.zeros(dimension)
    cont = 1
    
    dimension_repetidos = 250, 250
    repetidos = np.zeros(dimension_repetidos)
    contrepetidos = 1
    
    for x in range (dimension [0]):
        for y in range (dimension[1]):
            if imagen[x, y, 0] == 0:
                pass
            else:
                if imgetiquetada [x-1, y, 0] != 0 and imgetiquetada [x, y-1, 0] == 0:
                    imgetiquetada [x, y] = imgetiquetada [x-1 , y]
                    #print("si se metió al if")
                if imgetiquetada [x-1 , y, 0] == 0 and imgetiquetada [x, y-1, 0] != 0:
                    imgetiquetada [x, y] = imgetiquetada [x, y-1]
                    #print("si se metió al if 2 ")
                if imgetiquetada [x-1 , y, 0] != 0 and imgetiquetada [x, y-1, 0] != 0:
                    imgetiquetada [x, y] = imgetiquetada [x, y-1, 0]
                    
                    #En caso de que sean diferentes los numeros de alrededor, guardar los numeros para igualarlos
                    if imgetiquetada [x-1, y, 0] != imgetiquetada [x, y-1, 0]:
                        
                         repetido1 = imgetiquetada [x-1, y, 0]
                         repetido2 = imgetiquetada [x, y-1, 0]
                         print (contrepetidos)
                         print (repetido1)
                         print (repetido2)
                         if contrepetidos == 1:
                             repetidos [0, 0] = repetido1
                             repetidos [0, 1] = repetido2
                        
                         else:
                            for x in range (dimension_repetidos [0]):
                                for y in range (dimension_repetidos[1]):
                                    if repetidos [x, y] == repetido1:
                                        for y_zero in range (dimension_repetidos[1]):
                                            if repetidos[x, y_zero] == 0:
                                                repetidos[x, y_zero] = repetido2
                                                break
                       
                                    else:
                                        for x_zero in range (dimension_repetidos[0]):
                                            if repetidos[x_zero, 0] == 0:
                                                repetidos[x_zero, 0] = repetido1
                                                repetidos[x_zero, 1] = repetido2
                        
                        
                         contrepetidos = contrepetidos + 1
    
   
               
                        
                    
                    #imgetiquetada [x, y] = imgetiquetada [x, y-1, 0]
                    #A la derecha y la superior son ceros, pero sí hay hay un elemento en esa casilla   
                elif imgetiquetada [x-1, y, 0] == 0 and imgetiquetada [x, y-1, 0] == 0:
                    imgetiquetada [x, y] = cont                                             #Asigna a la casilla el valor del contador
                    cont = cont + 1 
                
                
                
                
                
                
    
    imgetiquetada = np.uint16(imgetiquetada)                   
    #return imgetiquetada           
    return imgetiquetada, repetidos          
    


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



bynori = blancoynegro(imgori)
etiquetada = etiquetas(bynori)


cv2.imshow('Imagen original', image_resize(imgori, height = 200))
cv2.moveWindow('Imagen original', 20, 20)

"""
cv2.imshow('Imagen original white patch', image_resize(originalwp, height = 200))
cv2.moveWindow('Imagen original white patch', 20, 240)

"""


cv2.imshow('Imagen original white patch a byn',image_resize(bynori, height = 200))
cv2.moveWindow('Imagen original white patch a byn', 20, 480)



cv2.waitKey(0)
cv2.destroyAllWindows()  