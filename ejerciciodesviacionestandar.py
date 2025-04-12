import numpy as np

estacion15 = [800, 830, 825, 795, 810, 815, 810, 820, 790 , 820, 805, 815, 800, 810 ,805]
estacioncampana = [800, 620, 50, 990, 980, 850, 985, 990, 890, 60, 100, 820, 950, 990, 980]



def calcular_estadisticas(ventas):
    promedio = np.mean(ventas)
    desviacion = np.std(ventas, ddof=1)  # Uso ddof=1 para calcular la desviación estándar muestral
    coef_variabilidad = desviacion / promedio
    return promedio, desviacion, coef_variabilidad

#calcular longitud
longitud_estacion15 = len(estacion15)
longitud_estacioncampana = len(estacioncampana)

print(longitud_estacion15)
print(longitud_estacioncampana)

#calcular promedio
media_estacion15 = sum(estacion15) / longitud_estacion15
media_estacioncampana = sum(estacioncampana) / longitud_estacioncampana

print(media_estacion15)
print(media_estacioncampana)

#calcular desviacion estandar 
promedio_15, desviacion_15, coef_variabilidad_15 = calcular_estadisticas(estacion15)
promedio_campana, desviacion_campana, coef_variabilidad_campana = calcular_estadisticas(estacioncampana)

# Evaluacion de la demanda
demanda_15 = "Determinista" if coef_variabilidad_15 < 0.2 else "Probabilista"
demanda_campana = "Determinista" if coef_variabilidad_campana < 0.2 else "Probabilista"


print(f"Estación La 15: Promedio={promedio_15:.2f}, Desviación={desviacion_15:.2f}, Coef. Variabilidad={coef_variabilidad_15:.4f} ({demanda_15})")
print(f"Estación Campana: Promedio={promedio_campana:.2f}, Desviación={desviacion_campana:.2f}, Coef. Variabilidad={coef_variabilidad_campana:.4f} ({demanda_campana})")
