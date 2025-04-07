import math

"""
    D = 50 unidades diarias
    K = 20$
    h = 0.35 por unidad semanal
    L = 1 semana
"""

# Calcular EOQ
def calcular_lote(D, K, h):
    EOQ = ((2 * D * K) / h) ** 0.5
    return int(EOQ)

# Calcular punto de reorden clásico
def calcular_R(D, L):
    ROP = D * L
    return ROP 

# Calcular punto de reorden alternativo
def calcular_R_2(D, L, T):
    m = 0
    while True:
        if L - m * T > 0 and L - (m + 1) * T <= 0:
            R = D * (L - m * T)
            break
        m += 1
    return R

# Calcular tiempo entre pedidos (T)
def calcular_T(K, D, h):
    T = math.sqrt((2 * K) / (D * h))
    return T

# Datos
h = 0.35    
demanda_diaria = 50
costo_ordenar = 20
plazo_entrega = 1  # semanas
demanda_semanal = demanda_diaria * 7

# Calcular EOQ y T
EOQ = calcular_lote(demanda_semanal, costo_ordenar, h)
T = calcular_T(costo_ordenar, demanda_semanal, h)

# Calcular punto de reorden según T
if T > plazo_entrega:
    ROP = calcular_R(demanda_semanal, plazo_entrega)
else:
    ROP = calcular_R_2(demanda_semanal, plazo_entrega, T)

# Mostrar resultados
print(f"Cantidad económica de pedido Q: {EOQ} unidades")
print(f"Punto de reorden: {round(ROP, 2)} unidades")
