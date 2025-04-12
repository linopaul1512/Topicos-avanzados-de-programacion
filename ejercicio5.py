"""
Una empresa local de contabilidad en Smalltown pide cajas de discos flexibles(10 discos por caja) a un almac´en en Megap´olis. El precio por caja que cobra el
almac´en depende del n´umero de cajas compradas (ver tabla). La empresa de contabilidad utiliza 10000 discos flexibles por a˜no. Se supone que el costo de un pedido son 100
d´olares. El ´unico costo de retenci´on es el costo de oportunidad del capital, se supone es
20 % por a˜no.Cada vez que se hace un pedido de discos, ¿Cu´antas cajas deben pedir?
¿Cu´antos pedidos se har´an al a˜no?¿Cu´al es el costo anual de satisfacer las necesidades
de discos de la empresa de contabilidad?
"""

import pandas as pd
import math

# Definir los datos en un diccionario
data = {
    'bi': [0, 100, 300],
    'q': ['q', 'q', 'q'],
    'b2': [100, 300, float('inf')],
    'P': [50, 49, 48.5],
    'h': [10, 9.8, 9.7],
    'k': [100, 100, 100],
    'D': [1000, 1000, 1000]
}

# Creo un DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Función para calcular la cantidad económica de pedido (Q)
def calcular_Q(D, k, h):
    return math.sqrt((2 * D * k) / h)

# Función para calcular el costo total (Cost)
def calcular_TC(q, p, D, k, h):
    # Costo de compra
    costo_compra = D * p
    # Costo de preparación (cuántos pedidos se hacen)
    num_pedidos = D / q
    costo_pedido = num_pedidos * k
    # Costo de retención
    costo_retencion = (q / 2) * h
    # Costo total
    return costo_compra + costo_pedido + costo_retencion

# Aplicar las funciones para cada fila
df['Q'] = df.apply(lambda row: calcular_Q(row['D'], row['k'], row['h']), axis=1)
df['Costo Total'] = df.apply(lambda row: calcular_TC(row['Q'], row['P'], row['D'], row['k'], row['h']), axis=1)

# Mostrar el DataFrame con las columnas EOQ y Costo Total
print(df)


    

    