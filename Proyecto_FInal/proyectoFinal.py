import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Generar los 4 vectores de 40 datos cada uno entre [80,100]
vectores = np.random.randint(80, 101, (4, 40))
print("4 vectores de demanda (valores entre 80 y 100):\n", vectores)

# Paso 2: Determinar si cada vector representa una demanda determinista o probabilística
tipos_demanda = []
for v in vectores:
    if np.all(v == v[0]):
        tipos_demanda.append("Determinista")
    else:
        tipos_demanda.append("Probabilística")

# Mostrar resultado
for i, tipo in enumerate(tipos_demanda):
    print(f"Vector {i+1}: Demanda {tipo}")


# Paso 3: Gráfico de las demandas
plt.figure(figsize=(10, 6))
for i in range(4):
    plt.plot(vectores[i], marker='o', label=f"Vector {i+1} - {tipos_demanda[i]}")

plt.title("Demanda: Determinista vs Probabilística")
plt.xlabel("Índice del dato")
plt.ylabel("Valor de la demanda")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


uso_anual = np.random.randint(5000, 20001, (4, 40))  # 4 vectores de uso anual
costo_unitario = np.random.uniform(5, 10, (4, 40))   # 4 vectores de costo unitario

# Valor total anual para cada producto
valor_anual = vectores * uso_anual * costo_unitario

clasificaciones = []

for i in range(4):
    valores = valor_anual[i]
    indices_ordenados = np.argsort(-valores)  # Orden descendente
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

    # Volver a poner la clasificación en el orden original
    clasif_final = [""] * 40
    for j, idx in enumerate(indices_ordenados):
        clasif_final[idx] = clasificacion[j]
    clasificaciones.append(clasif_final)

# Mostrar clasificación ABC del primer vector como ejemplo
print("\nClasificación ABC (primer vector):")
for i in range(40):
    print(f"Producto {i+1}: Clase {clasificaciones[0][i]}")

# Gráfico de barras: cantidad de productos por clase para cada vector


fig, axs = plt.subplots(2, 2, figsize=(10, 8))
for i in range(4):
    ax = axs[i//2, i%2]
    clases = clasificaciones[i]
    valores, conteo = np.unique(clases, return_counts=True)
    ax.bar(valores, conteo, color=["red", "orange", "green"])
    ax.set_title(f"Vector {i+1} - Clasificación ABC")
    ax.set_xlabel("Clase")
    ax.set_ylabel("Cantidad")

plt.tight_layout()
plt.show()
