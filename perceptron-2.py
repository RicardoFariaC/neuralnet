# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:06:21 2022

@author: ricar
"""
import numpy as np


entradas = np.array([-1, 7, 5])
pesos = np.array([0.8, 0.1, 0])


def soma(e, p):
    return e.dot(p)
# dot product - produto escalar        


def stepFunc(soma):
    if soma >= 1:
        return 1
    return 0


s = soma(entradas, pesos)

result = stepFunc(s)
