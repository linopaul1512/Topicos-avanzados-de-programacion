import math

def determinar_medidas_desempeño():
    
    print("Ingrese los datos en el siguiente orden dentro de un vector:")
    print("[media por hora (µ), Tiempo promedio de llegada (λ), Tiempo promedio en cola (Wq]")
    # 60 , 45,  3 
    # µ    λ   Wq   

    datos = list(map(float, input("Ingrese los valores separados por coma: ").split(',')))
    
    # Le asignamoss variables a las pocisiones del vector
    µ = datos[0]  
    λ = datos[1] 
    Wq = datos[2] 
    
    W = 1 / (µ- λ) * 60
    P = λ / µ
    Lq = (λ * P) / (µ - λ)
    L = λ / (µ - λ)

    print(f"Tiempo promedio que un cliente pasa en el sistema (en minutoss): {W:.2f}")
    print(f"Numero promedio de clientes en la cola: {Lq:.2f}") 
    print(f"Numero promedio de clientes en el sistemqa  en el momento dado  ): {L:.2f}") 

    
# Ejecutar la función
determinar_medidas_desempeño()
