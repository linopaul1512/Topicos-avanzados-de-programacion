import math

def modelo_descuento_cantidad():
    print("Ingrese los datos en el siguiente orden dentro de un vector:")
    print("[Costo de ordenar (K), Demanda anual (D), Costo de almacenaje % (h)]")
    datos = list(map(float, input("Ingrese los valores separados por coma: ").split(',')))

    # Extraer los datos
    K = datos[0]  # Costo de ordenar
    D = datos[1]  # Demanda anual
    h_percent = datos[2] / 100  # Convertimos % a decimal

    # Pedir al usuario cuántos niveles de descuento quiere ingresar
    n_descuentos = int(input("\n¿Cuántos rangos de descuento desea ingresar? "))

    tabla = []

    print("Ingrese los rangos de la tabla en el siguiente formato:")
    print("cantidad mínima, cantidad máxima (o inf), precio unitario")
    print("Ejemplo: 0,99,20.00")

    for i in range(n_descuentos):
        entrada = input(f"Ingrese el rango #{i+1}: ")
        partes = entrada.split(',')

        b_min = int(partes[0])
        b_max = float('inf') if partes[1].lower() == 'inf' else int(partes[1])
        precio = float(partes[2])

        tabla.append((b_min, b_max, precio))

    # Calcular EOQ, validar rango y calcular costo total
    opciones = []

    for (b_min, b_max, precio_unitario) in tabla:
        h = h_percent * precio_unitario  # h dinámico según el precio
        EOQ = math.sqrt((2 * K * D) / h)

        # Verificar si EOQ es admisible en el rango
        if b_min <= EOQ < b_max:
            q = EOQ
        else:
            q = b_min if EOQ < b_min else EOQ

        if q == 0:
            print(f"Aviso: El rango ({b_min}, {b_max}) resultó en una cantidad inválida (q=0), se omite.")
            continue

        CT = (K * D / q) + (h * q / 2) + (precio_unitario * D)
        opciones.append((q, precio_unitario, CT))

    # Seleccionar la opción con menor costo total
    mejor_opcion = min(opciones, key=lambda x: x[2])

    print("\n***** RESULTADOS *****")
    print(f"Cantidad óptima de pedido (q): {mejor_opcion[0]:.2f} unidades")
    print(f"Frecuencia óptima de pedidos por año: {D / mejor_opcion[0]:.2f}")
    print(f"Precio por unidad correspondiente: ${mejor_opcion[1]:.2f}")
    print(f"Costo total anual: ${mejor_opcion[2]:.2f}")

# Ejecutar función
modelo_descuento_cantidad()
