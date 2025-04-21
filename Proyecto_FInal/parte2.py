import math
import matplotlib.pyplot as plt
import random


def modelo_descuento_simple(K, D, h_percent, precios_descuento):
    n_descuentos = int(input("\n¿Cuántos rangos de descuento desea ingresar? "))

    tabla = []
    print("Ingrese los rangos en formato: cantidad mínima, cantidad máxima (o inf), precio unitario")
    for i in range(n_descuentos):
        entrada = input(f"Ingrese el rango #{i+1}: ")
        partes = entrada.split(',')

        b_min = int(partes[0])
        b_max = float('inf') if partes[1].lower() == 'inf' else int(partes[1])
        precio = float(partes[2])

        tabla.append((b_min, b_max, precio))

    opciones = []
    qs = []
    cts = []

    for (b_min, b_max, precio_unitario) in tabla:
        h = h_percent * precio_unitario
        EOQ = math.sqrt((2 * K * D) / h)

        if b_min <= EOQ < b_max:
            q = EOQ
        else:
            q = b_min if EOQ < b_min else EOQ

        if q == 0:
            print(f"Aviso: El rango ({b_min}, {b_max}) resultó en q=0, se omite.")
            continue

        CT = (K * D / q) + (h * q / 2) + (precio_unitario * D)
        opciones.append((q, precio_unitario, CT))
        qs.append(q)
        cts.append(CT)


    return qs, cts

def modelo_con_faltante(K, D, h, p):
    Q = math.sqrt((2 * K * D * p) / (h * (p + h)))
    S = (p / (p + h)) * Q
    CT = (K * D / Q) + (h * (Q - S)**2 / (2 * Q)) + (p * S**2 / (2 * Q))
    return Q, S, D / Q, CT

def clasificacion_ABC(productos):
    productos.sort(key=lambda x: x[2] * x[1], reverse=True)
    total_valor = sum(p[2] * p[1] for p in productos)

    acumulado = 0
    clasificacion = []

    for producto in productos:
        valor = producto[2] * producto[1]
        acumulado += valor
        porcentaje = acumulado / total_valor

        if porcentaje <= 0.8:
            clase = 'A'
        elif porcentaje <= 0.95:
            clase = 'B'
        else:
            clase = 'C'

        clasificacion.append((producto[0], producto[1], producto[2], clase))

    return clasificacion

# ------------------------------
# GRÁFICO
# ------------------------------

def graficar_costos(qs_list, cts_list, etiquetas):
    plt.figure(figsize=(10, 6))
    for i in range(len(qs_list)):
        plt.plot(qs_list[i], cts_list[i], label=etiquetas[i], marker='o')

    plt.xlabel("Cantidad de pedido (Q)")
    plt.ylabel("Costo Total Anual (CT)")
    plt.title("Comparación de Costos por Modelo")
    plt.legend()
    plt.grid(True)
    plt.show()

# ------------------------------
# MENÚ INTERACTIVO
# ------------------------------

def ejecutar_menu():
    print("=== CÁLCULO DE MODELOS DE INVENTARIO ===")
    K = float(input("Costo de ordenar (K): "))
    D = float(input("Demanda anual (D): "))
    h_percent = float(input("Costo de almacenaje (%): ")) / 100

    print("\nSeleccione el modelo a calcular:")
    print("1. Descuento simple")
    print("2. Modelo con faltante")
    print("3. Clasificación ABC")

    modelo = int(input("Opción: "))

    if modelo == 1:
        print("\nIngrese los rangos de descuento como mínimo, máximo, precio (use 'inf' si no hay tope superior)")
        n = int(input("¿Cuántos niveles de precio?: "))
        descuentos = []
        for i in range(n):
            entrada = input(f"Rango #{i + 1} (ej: 0,99,20): ")
            partes = entrada.split(',')
            b_min = int(partes[0])
            b_max = float('inf') if partes[1].lower() == 'inf' else int(partes[1])
            precio = float(partes[2])
            descuentos.append((b_min, b_max, precio))

        resultados, qs, cts = modelo_descuento_simple(K, D, h_percent, descuentos)

        print("\n--- RESULTADOS DESCUENTO SIMPLE ---")
        for r in resultados:
            print(f"Q = {r[0]:.2f} | Frecuencia = {r[1]:.2f} | Precio unitario = {r[2]} | CT = {r[3]:.2f}")

        graficar_costos([qs], [cts], ["Descuento Simple"])

    elif modelo == 2:
        p = float(input("Costo de faltante por unidad (p): "))
        h = h_percent * 10  # Supongamos precio unitario de 10
        Q, S, T, CT = modelo_con_faltante(K, D, h, p)

        print("\n--- RESULTADOS MODELO CON FALTANTE ---")
        print(f"Cantidad a pedir (Q): {Q:.2f}")
        print(f"Nivel de servicio (S): {S:.2f}")
        print(f"Frecuencia de pedidos (T): {T:.2f}")
        print(f"Costo total anual: {CT:.2f}")

        graficar_costos([[Q]], [[CT]], ["Modelo con Faltante"])

    elif modelo == 3:
        print("\nGenerando 20 productos aleatorios...")
        productos = []
        for i in range(1, 21):
            id_prod = f"P{i}"
            demanda = random.randint(5000, 20000)
            precio = round(random.uniform(5, 10), 2)
            productos.append((id_prod, demanda, precio))

        clasificados = clasificacion_ABC(productos)

        print("\n--- CLASIFICACIÓN ABC ---")
        for c in clasificados:
            print(f"{c[0]} | Demanda: {c[1]} | Precio: {c[2]} | Clase: {c[3]}")

    else:
        print("Opción inválida")

# ------------------------------
# EJECUTAR
# ------------------------------
ejecutar_menu()
