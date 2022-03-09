# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:18:36 2022

@author: ricar
"""
# Implementando o treinamento do ajuste de pesos
import numpy as np

# OPERADOR E (AND)

# entradas = np.array([[0,0], [0,1], [1,0], [1, 1]])
# saidas = np.array([0, 0, 0, 1])

# OPERADOR OU (OR)

# entradas = np.array([[0,0], [0,1], [1,0], [1, 1]])
# saidas = np.array([0, 1, 1, 1])

# OPERADOR XOU (XOR)

entradas = np.array([[0,0], [0,1], [1,0], [1, 1]])
saidas = np.array([0, 1, 1, 0])
pesos = np.array([0.0, 0.0])


taxaAprendizagem = 0.1

def stepFunc(soma):
    if soma >= 1:
        return 1
    return 0

def calcularSaida(registro):
    s = registro.dot(pesos)
    return stepFunc(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calcularSaida(np.array([entradas[i]]))
            err = abs(saidas[i] - saidaCalculada)
            erroTotal += err
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * err)
                print(f"Peso atualizado{entradas[i]}: " + str(round(pesos[j], 2)))
        print("Total de erros: " + str(erroTotal))

treinar()
print("Rede neural treinada")
print(calcularSaida(entradas[0]))
print(calcularSaida(entradas[1]))
print(calcularSaida(entradas[2]))
print(calcularSaida(entradas[3]))
