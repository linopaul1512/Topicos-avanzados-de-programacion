# Datos comunes
costo_preparacion = 20  # K ($ por pedido)
costo_almacenamiento_diario = 0.02  # h1 (por unidad por día)

# Política 1
pedido1 = 150  # y: unidades por pedido
punto_reorden1 = 50  # unidades
tiempo_entre_pedidos1 = 10  # días

# Política 2
pedido2 = 200  # y: unidades por pedido
punto_reorden2 = 75  #unidades
tiempo_entre_pedidos2 = 15  # días

def calcular_costo_total(K, D, y, h1, dias_pedido):
    demanda = D / dias_pedido  # D = demanda diaria basada en punto de reorden y días    
    # CT= K D/y + h1 y/2
    costo_total = (K * demanda) / y + (h1 * y) / 2
    return costo_total

# Calcular costos con nueva fórmula
costo_total1 = calcular_costo_total(costo_preparacion, punto_reorden1, pedido1, costo_almacenamiento_diario, tiempo_entre_pedidos1)
costo_total2 = calcular_costo_total(costo_preparacion, punto_reorden2, pedido2, costo_almacenamiento_diario, tiempo_entre_pedidos2)

print("Costo total con Política 1 (pedido de 150 unidades): ${:.2f}".format(costo_total1))
print("Costo total con Política 2 (pedido de 2 unidades): ${:.2f}".format(costo_total2))

# Recomendación
if costo_total1 < costo_total2:
    print("\n Se recomienda adoptar la Política 1.")
else:
    print("\n Se recomienda adoptar la Política 2.")
