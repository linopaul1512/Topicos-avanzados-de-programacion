import math

def modelo_descuento_cantidad():
    print("Ingrese los datos en el siguiente orden dentro de un vector:")
    print("[Costo de ordenar (K), Demanda anual (D), Costo de almacenaje % (h)]")
     # 40, 460, 10
    datos = list(map(float, input("Ingrese los valores separados por coma: ").split(',')))
    
    # Extraer los datos
    K = datos[0]  # Costo de ordenar
    D = datos[1]  # Demanda anual
    h_percent = datos[2] / 100  # Convertimos % a decimal

    # Tabla de descuentos por cantidad
    tabla = [
        (0, 99, 20.00),
        (100, 199, 19.50),
        (200, 499, 19.00),
        (500, float('inf'), 18.75)
    ]
    
    opciones = []

    for (b_min, b_max, precio_unitario) in tabla:
        h = h_percent * precio_unitario  # h calculado dinámicamente según el precio
        print("esta es una impresuion", h)
        EOQ = math.sqrt((2 * K * D) / h)
        
        # Verificar si EOQ es admisible
        if b_min <= EOQ < b_max:
            q = EOQ
        else:
            q = b_min if EOQ < b_min else EOQ
        
        # Costo total
        CT = (K * D / q) + (h * q / 2) + (precio_unitario * D)
        
        opciones.append((q, precio_unitario, CT))

    # Seleccionar la mejor opción (menor costo total)
    mejor_opcion = min(opciones, key=lambda x: x[2])

    print("\n*****RESULTADOS *****")
    print(f"Cantidad óptima de pedido (q): {mejor_opcion[0]:.2f} unidades")
    print(f"Frecuencia óptima de pedidos por año: {D / mejor_opcion[0]:.2f}")
    print(f"Precio por unidad correspondiente: ${mejor_opcion[1]:.2f}")
    print(f"Costo total anual: ${mejor_opcion[2]:.2f}")

# Ejecutar función
modelo_descuento_cantidad()
