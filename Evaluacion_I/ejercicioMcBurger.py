import math

def determinar_politica_optima():
    
    print("Ingrese los datos en el siguiente orden dentro de un vector:")
    print("[Costo de ordenar (K), Demanda semanal (D), Costo por libra de carne (c), Tiempo que tarda el pedido (L) , Costo de almacenaje por libra al día(h)]")
    # 20, 300, 0.80, 0, 0.03
    # k    D    c    L   h

    datos = list(map(float, input("Ingrese los valores separados por coma: ").split(',')))
    
    # Le asignamoss variables a las pocisiones del vector
    K = datos[0]  
    D = datos[1] 
    c = datos[2] 
    L = datos[3]
    h = datos[4] 
    h_semanal_unitaria = h  * 7
    D_diaria = D / 7 #demanda semanal entre los 7 dias de la semana

    Q =   ((2 * D_diaria * K) / h) ** 0.5
    Cost_Q = (c * D) + (K * D / Q) + (1 / 2 * h_semanal_unitaria * Q)

    print(f"Costo total semanal semanal de inventario: ${Cost_Q:.2f}") #290
    print(f"Politica optima por inventario(Cantidad de reordenar cada vez): ${Q:.2f}") #240

# Ejecutar la función
determinar_politica_optima()
