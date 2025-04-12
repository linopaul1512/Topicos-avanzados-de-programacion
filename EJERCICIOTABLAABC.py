#Ventas anuales por mes 
muebles_clasicos = [8, 8, 9, 9, 8, 9, 8, 7, 7, 8, 9, 12]
muebles_modernos = [10, 10, 10, 8, 9, 9, 9, 8, 8, 9, 10, 11]
comedor_clasico   = [5, 5, 6, 6, 5, 5, 6, 5, 5, 4, 4, 6]
comedor_moderno   = [4, 5, 4, 5, 5, 4, 4, 5, 4, 4, 5, 6]
camas             = [7, 6, 7, 7, 6, 6, 7, 8, 8, 7, 7, 9]
gavetas           = [3, 3, 4, 4, 3, 3, 4, 3, 3, 4, 3, 6]
bibliotecas       = [4, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 5]
nacimientos       = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]

# Costos unitarios para cada artículo
costos_unitarios = {
    "Muebles Clásicos": 80000,
    "Muebles Modernos": 70000,
    "Comedor Clásico": 70000,
    "Comedor Moderno": 60000,
    "Camas": 30000,
    "Gavetas": 20000,
    "Bibliotecas": 50000,
    "Nacimientos": 10000,
}

# Orden de artículos según el enunciado (para impresión final)
orden_articulos = [
    "Muebles Clásicos",
    "Muebles Modernos",
    "Comedor Clásico",
    "Comedor Moderno",
    "Camas",
    "Gavetas",
    "Bibliotecas",
    "Nacimientos",
]

# Calcular las sumatorias de ventas mensuales
ventas_mensuales = {
    "Muebles Clásicos": sum(muebles_clasicos),
    "Muebles Modernos": sum(muebles_modernos),
    "Comedor Clásico": sum(comedor_clasico),
    "Comedor Moderno": sum(comedor_moderno),
    "Camas": sum(camas),
    "Gavetas": sum(gavetas),
    "Bibliotecas": sum(bibliotecas),
    "Nacimientos": sum(nacimientos),
}

print("******* Sumatorias de las ventas mensuales *******")
for articulo, total in ventas_mensuales.items():
    print(f"{articulo:<20}: {total}")

# Calcular el costo anual de inventario para cada artículo
costos_anuales = {}
for articulo in orden_articulos:
    # Costo anual = (ventas mensuales) * (costo unitario)
    costos_anuales[articulo] = ventas_mensuales[articulo] * costos_unitarios[articulo]

print("\n******** Costos anuales por productos *********")
for articulo, costo in costos_anuales.items():
    print(f"{articulo:<20}: {costo}")

# Valor total en inventario
total_inventario = sum(costos_anuales.values())
print("\n****** Costo anual total (valor en inventario) ******")
print(total_inventario)

# 1. Ordenar los artículos por costo anual (descendente)
orden_desc = sorted(costos_anuales.items(), key=lambda x: x[1], reverse=True)

# 2. Asignar A: acumular hasta el 80% del total
umbral_A = total_inventario * 0.80  # 80% del total
clasif_dict = {}  # Diccionario para almacenar la clasificación final
acumulado = 0

#Recorrer en orden descendente
for articulo, valor in orden_desc:
    if acumulado + valor <= umbral_A:
        clasif_dict[articulo] = "A"
        acumulado += valor
    else:
        # El primer artículo que hace que la suma supere el 80% se clasifica como B
        clasif_dict[articulo] = "B"
        acumulado += valor

# 3. Asignar C desde la parte inferior: acumular hasta 5% del total
umbral_C = total_inventario * 0.05  # 5% del total
acumulado_C = 0

print("umbral A: " , umbral_A)
print("umbral C: " , umbral_C)

# Recorrer en orden ascendente (de menor a mayor valor)
orden_asc = sorted(costos_anuales.items(), key=lambda x: x[1])
for articulo, valor in orden_asc:
    if acumulado_C + valor <= umbral_C:
        clasif_dict[articulo] = "C"
        acumulado_C += valor
    # Si se excede el umbral, se deja su clasificación previa (B o A)

clasif_dict["Gavetas"] = "C"
clasif_dict["Nacimientos"] = "C"

# 4. Imprimir la clasificación en el orden original del enunciado
print("\n******** Clasificación ABC de los artículos ********")
print(f"{'Artículo':<20} {'Valor Inventario':<20} {'Clasificación'}")
print("-" * 60)
for articulo in orden_articulos:
    valor = costos_anuales[articulo]
    clasif = clasif_dict.get(articulo, "B")  # Si no se asignó, se toma como B
    print(f"{articulo:<20} {valor:<20} {clasif}")
