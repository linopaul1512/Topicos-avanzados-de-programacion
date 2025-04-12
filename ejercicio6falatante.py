import math


"""
    K = 75
    D= 13 computadoras por semana 
    h = 20%
    c= 3000
    L= 0.5
    p = 200
    
    """


def modelo_con_faltantes():
    print("Ingrese los datos en el siguiente orden dentro de un vector:")
    print("[Costo de ordenar K, Demanda semanal D, Costo de almacenaje (%), Costo por unidad, Tiempo de entrega en semanas L, costo por faltante p]")
    # 75, 13, 20, 3000, 0.5, 200

    datos = list(map(float, input("Ingrese los valores separados por coma: ").split(',')))

    # Asignación de variables
    K = datos[0]  # Costo por pedido
    D_semanal = datos[1]  # Demanda semanal
    D = D_semanal * 52  # Demanda anual
    h = (datos[2] / 100) * datos[3]  # Costo de mantenimiento anual por unidad
    C = datos[3]  # Costo por unidad
    L = datos[4]  # Tiempo de entrega en semanas
    p = datos[5]  # Costo por faltante

    # Cantidad económica con faltantes permitidos
    Q = math.sqrt((2 * D * K * (h + p)) / (h * p))
    S = (p / (h + p)) * Q  # Nivel de inventario máximo
    B = Q - S  # Faltantes permitidos
    R = D_semanal * L  # Punto de reorden

    print(f"\nCantidad óptima de pedido (Q): {Q:.2f}")
    print(f"Nivel máximo de inventario (S): {S:.2f}")
    print(f"Faltantes permitidos: {B:.2f}")
    print(f"Punto de reorden (R): {R:.2f}")

modz


