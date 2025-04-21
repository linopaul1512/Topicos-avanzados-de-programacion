import numpy as np
import matplotlib.pyplot as plt

# Preguntar cuántos vectores desea el usuario
cantidad_vectores = int(input("¿Cuántos vectores desea generar? "))

# Pedir el tamaño de cada vector
cantidad_elemental = int(input("Introduzca la cantidad de elementos que quiera generar "))

# Generar vectores de 40 elementos con valores entre 80 y 100
vectores = np.random.randint(80, 101, (cantidad_vectores, cantidad_elemental))
print(f"\n{cantidad_vectores} vectores de demanda (valores entre 80 y 100):\n", vectores)

# Determinar tipo de demanda: determinista o probabilística
tipos_demanda = []
for v in vectores:
    if np.all(v == v[0]):
        tipos_demanda.append("Determinista")
    else:
        tipos_demanda.append("Probabilística")

# Mostrar tipo de demanda
for i, tipo in enumerate(tipos_demanda):
    print(f"Vector {i+1}: Demanda {tipo}")



# Generar uso anual y costo unitario aleatorio para cada producto
uso_anual = np.random.randint(5000, 20001, (cantidad_vectores, 40))
costo_unitario = np.random.uniform(5, 10, (cantidad_vectores, 40))

# Calcular valor total anual
valor_anual = vectores * uso_anual * costo_unitario

clasificaciones = []

for i in range(cantidad_vectores):
    valores = valor_anual[i]
    indices_ordenados = np.argsort(-valores)
    valores_ordenados = valores[indices_ordenados]
    suma_total = np.sum(valores_ordenados)
    acumulado = np.cumsum(valores_ordenados)
    porcentaje = acumulado / suma_total

    clasificacion = []
    for p in porcentaje:
        if p <= 0.80:
            clasificacion.append("A")
        elif p <= 0.95:
            clasificacion.append("B")
        else:
            clasificacion.append("C")

    clasif_final = [""] * cantidad_elemental
    for j, idx in enumerate(indices_ordenados):
        clasif_final[idx] = clasificacion[j]
    clasificaciones.append(clasif_final)

# Mostrar clasificación ABC de todos los vectores
for v in range(cantidad_vectores):
    print(f"\nClasificación ABC - Vector {v+1}:")
    for i in range(cantidad_elemental):
        print(f"Producto {i+1}: Clase {clasificaciones[v][i]}")

# Gráfico de las demandas
plt.figure(figsize=(10, 6))
for i in range(cantidad_vectores):
    plt.plot(vectores[i], marker='o', label=f"Vector {i+1} - {tipos_demanda[i]}")

plt.title("Demanda: Determinista vs Probabilística")
plt.xlabel("Índice del dato")
plt.ylabel("Valor de la demanda")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de barras: cantidad de productos por clase
columnas = 2
filas = (cantidad_vectores + 1) // columnas

fig, axs = plt.subplots(filas, columnas, figsize=(12, 4 * filas))
axs = axs.flatten() if cantidad_vectores > 1 else [axs]

for i in range(cantidad_vectores):
    ax = axs[i]
    clases = clasificaciones[i]
    valores, conteo = np.unique(clases, return_counts=True)
    ax.bar(valores, conteo, color=["red", "orange", "green"])
    ax.set_title(f"Vector {i+1} - Clasificación ABC")
    ax.set_xlabel("Clase")
    ax.set_ylabel("Cantidad")

plt.tight_layout()
plt.show()
