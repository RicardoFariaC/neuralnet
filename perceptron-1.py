# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 16:56:10 2022

@author: ricar
"""

entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]


def soma(e, p):
    s = 0
    for i in range(3):
        #print(entradas[i])
        #print(pesos[i])
        s += e[i] * p[i]
    return s
        

def stepFunc(soma):
    if soma >= 1:
        return 1
    return 0

s = soma(entradas, pesos)

result = stepFunc(s)

