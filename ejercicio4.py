import math

# Datos del usuario
consumo_anual = [4000, 1400, 10000, 5000, 4000, 5000, 3000, 5500, 6000, 2500,
                 4500, 1000, 5500, 9000, 3000, 2500, 1000, 1900, 5600, 1500]

costo_unitario = [1.25, 7.00, 10.00, 1.50, 0.50, 13.00, 0.75, 1.50, 5.25, 2.00,
                  10.00, 15.00, 25.50, 30.00, 15.00, 3.00, 1.25, 7.00, 30.50, 14.00]

# Crear vector calculando valor anual por artículo (consumo * costo unitario)
valor_anual = [c * p for c, p in zip(consumo_anual, costo_unitario)] #zip es un operador de tuplas

# Total inventario
total_inventario = sum(valor_anual)

# Orden descendente por valor
articulos_ordenados = sorted(enumerate(valor_anual), key=lambda x: x[1], reverse=True)

# Clasificación ABC
clasificacion = [""] * len(valor_anual)
acumulado = 0
umbral_A = 0.80 * total_inventario
umbral_C = 0.05 * total_inventario

# A
for idx, valor in articulos_ordenados:
    if acumulado + valor <= umbral_A:
        clasificacion[idx] = "A"
        acumulado += valor
    else:
        break

# B para los que aún no tienen clasificación
for idx, valor in articulos_ordenados:
    if clasificacion[idx] == "":
        clasificacion[idx] = "B"

# C desde el final
acumulado_C = 0
for idx, valor in sorted(enumerate(valor_anual), key=lambda x: x[1]):
    if acumulado_C + valor <= umbral_C:
        clasificacion[idx] = "C"
        acumulado_C += valor

# Resultado
print("Art Consumo\tCosto U.\tValor Anual\tClasificación") #/t es para simular sangria en una tabla
for i in range(len(valor_anual)):
    print(f"{i+1:<3}\t{consumo_anual[i]:<7}\t{costo_unitario[i]:<9}\t{valor_anual[i]:<12.2f}\t{clasificacion[i]}")
