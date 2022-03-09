# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:35:43 2022

@author: ricar
"""

# Implementação da função sigmoide - y = 1/(1 + e^-x)

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

#a = sigmoid(0.5)
#a_deriv = sigmoidDerivada(a)
# a = sigmoid(50) # Trabalha com um gráfico que varia de, aproximadamente, 1 e 0.

# OPERADOR XOR

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([[0], [1], [1], [0]])

#pesosCE = np.array([[-0.424, -0.740, -0.961], [0.358, -0.577, -0.469]])
#pesosCO = np.array([[-0.017], [-0.893], [0.148]])

pesosCE = 2 * np.random.random((2, 3)) - 1
pesosCO = 2 * np.random.random((3, 1)) - 1

epocas = 100000
taxaAprendizagem = 1
momento = 1

for j in range(epocas):
    camadaEntrada = entradas 
    somaSinapseCE = np.dot(camadaEntrada, pesosCE)
    
    camadaOculta = sigmoid(somaSinapseCE)
    somaSinapseCO = np.dot(camadaOculta, pesosCO)
    
    camadaSaida = sigmoid(somaSinapseCO)
    errCamadaSaida = saidas - camadaSaida # err = camadaespera - camadacalculada
    mediaAbsoluta = np.mean(np.abs(errCamadaSaida))
    print(f"Erro: {str(mediaAbsoluta)}")


    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = errCamadaSaida * derivadaSaida
    
    pesosCOTransposta = pesosCO.T
    saidaXPeso = deltaSaida.dot(pesosCOTransposta)
    deltaCO = saidaXPeso * sigmoidDerivada(camadaOculta)

    # Backpropagation equation
    # w(n+1) = [w(n) * momentum] + [input * delta * learning_rate]

    camadaOcultaTransposta = camadaOculta.T
    pesosNovosCO = camadaOcultaTransposta.dot(deltaSaida)
    pesosCO = (pesosCO * momento) + (pesosNovosCO * taxaAprendizagem)

    camadaEntradaTransposta = camadaEntrada.T
    pesosNovosCE = camadaEntradaTransposta.dot(deltaCO)
    pesosCE = (pesosCE * momento) + (pesosNovosCE * taxaAprendizagem)
    
    
    





