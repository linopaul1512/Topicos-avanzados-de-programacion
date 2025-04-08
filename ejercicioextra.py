import math
import scipy.statemodels
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#Calcular Experanza
def calcular_Esperanza(D, M):
    #M = E(D) = n p(D)
    E = M * D
    return E
    
def calcular_Q(K, E, D, h):
    Q = math.sqrt(2 * K* (E * D) / h)
    return Q

def P_acolumado(h, Q, E, c):
    P = (h + Q) / (c * E)
    
def buscar_valoresGauss():
    dato = abs(norm.ppf(0.005))