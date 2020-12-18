# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:11:31 2020

@author: Alexandre
"""

def diff_list(lista1,lista2):
    listaRetorno = []
    if(len(lista1) == 0):
        return listaRetorno
    if(len(lista2) == 0 and len(lista1) > 0):
        listaRetorno = lista1
        return listaRetorno   
    for a in lista1:
        if a not in lista2:
            listaRetorno.append(a)
    return listaRetorno
   


lista1 = [1,3,5,7,9]
lista2 = [1,11,7,77]
print(diff_list(lista1,lista2))


