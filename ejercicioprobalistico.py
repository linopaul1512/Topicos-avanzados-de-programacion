import math
import numpy as np
from scipy.stats import norm

def modelo_probabilistico():
    print("Ingrese los datos en el siguiente orden dentro de un vector:")
    print("[Demanda promedio diaria (d), Desviación estándar diaria (σ), Tiempo entrega (L), Costo pedido (K), Costo anual por unidad (h), Costo unidad (C), Nivel de servicio (%) ]")
    #20, 4, 5, 40, 8, 200, 95

    datos = list(map(float, input("Ingrese los valores separados por coma: ").split(',')))

    d = datos[0]  # Demanda promedio diaria
    sigma = datos[1]  # Desviación estándar de la demanda diaria
    L = datos[2]  # Tiempo de entrega (días)
    K = datos[3]  
    h = datos[4]  
    C = datos[5] 
    nivel_servicio = datos[6] / 100  # Nivel de servicio (porcentaje)

    D = d * 365  # Demanda anual
    Q = math.sqrt((2 * D * K) / h)  # Cantidad óptima de pedido
    Z = norm.ppf(nivel_servicio)
    R = (d * L) + (Z * sigma * math.sqrt(L))  

    print(f"\nCantidad óptima de pedido (Q): {Q:.2f}")
    print(f"Punto de reorden (R) con nivel de servicio del {nivel_servicio*100:.0f}%: {R:.2f}")
    

modelo_probabilistico()


