# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:19:57 2022

@author: Johan Lee
"""

import numpy as np

alfa = 0.5
dataset = np.array([[1, -1, -1, -1], 
                   [1,  1, -1, -1],
                   [1, -1,  1, -1],
                   [1,  1,  1,  
                    1]
                   ])

d = np.array([dataset[0, 3], dataset[1, 3], dataset[2, 3], dataset[3, 3]])
w = np.array([1, 1, 1])


for cont in range(10):
    
    if (cont % 4) == 0:
        cont=0
        
    if ((cont -1) % 4) == 0:
        cont=1
        
    if ((cont -2) % 4) == 0:
        cont=2
     
    if ((cont -3) % 4) == 0:
        cont=3
        
    x = np.array([dataset[cont, 0], dataset[cont, 1], dataset[cont, 2]])
    y = np.sign(np.dot(np.transpose(w), x))
    w =  w + (alfa*(d[cont]-y)*x)
    print ("Condiciones AND = ", x)
    print ("Resulado AND = ", y)
    print ("Valor (j+1) = ", w)
    input("Press Enter to continue...\n\n\n")
    