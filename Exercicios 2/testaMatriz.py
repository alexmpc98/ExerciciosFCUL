# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:54:44 2020

@author: Alexandre
"""

def testa_matriz(array):
    num = len(array[0])
    size = len(array)
    counter = 0
    for i in range(len(array)):
        if(len(array[i]) == num):
            counter = counter + 1
    if(counter == size):
        return (size,len(array[0]))
    return ()



array = [[-92.4]]
print(testa_matriz(array))
            
        
    
