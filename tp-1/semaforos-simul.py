import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros de la simulación
tiempo_simulacion = 200  # Tiempo total de la simulación en unidades arbitrarias
ciclo_semaforo_verde = 30
ciclo_semaforo_amarillo = 5
ciclo_semaforo_rojo = 10
ciclo_total = ciclo_semaforo_verde + ciclo_semaforo_amarillo + ciclo_semaforo_rojo
num_vehiculos_inicial = 25
tiempo_llegada_vehiculos = 15  # Tiempo promedio entre llegadas de vehículos

# Inicializa variables
tiempo_actual = 0
vehiculos = []  # Lista para almacenar la posición y el estado de los vehículos
semaforo_estado = 'verde'  # Estado inicial del semáforo
tiempo_semaforo = 0

# Función para actualizar el estado de los semáforos
def actualizar_estado_semaforo(tiempo):
    tiempo_en_ciclo = tiempo % ciclo_total # mantiene los valores siempre dentro de la duración de un (1) ciclo (rango de 0 a ciclo_total). La duración del ciclo está determinada por la sumatoria de los ciclos de cada color del semáforo (verde + amarillo + rojo)
    if tiempo_en_ciclo < ciclo_semaforo_verde:
        return 'verde'
    elif tiempo_en_ciclo < ciclo_semaforo_verde + ciclo_semaforo_amarillo:
        return 'amarillo'
    else:
        return 'rojo'

# Función para generar vehículos
def generar_vehiculos(tiempo_actual, num_vehiculos):
    for _ in range(num_vehiculos):
        # ahora mismo la suma con el tiempo_actual no tiene sentido, porque esta función sólo se ejecuta al inicio del programa. Tiene más sentido si la generación de vehículos se varias veces en el transcurso de la simulación.
        llegada = tiempo_actual + np.random.uniform(0, tiempo_llegada_vehiculos)
        vehiculos.append({'tiempo_llegada': llegada, 'estado': 'espera'})

# Inicialización de la simulación
generar_vehiculos(0, num_vehiculos_inicial)

# Almacenar datos para la visualización

###################################################################################################
# TO DO: pensar qué datos sin interesantes almacenar para mostrar en el resultado de la simulación
###################################################################################################

# Simulación
while tiempo_actual < tiempo_simulacion:
    semaforo_estado = actualizar_estado_semaforo(tiempo_actual)

    # TO DO: ver dónde agregar los datos para el resultado #

    # Actualizar vehículos
    for vehiculo in vehiculos:
        if (vehiculo['estado'] == 'espera' 
            and vehiculo['tiempo_llegada'] <= tiempo_actual # Sino: es un vehículo que aún no "llegó" en la simulación...
            and semaforo_estado == 'verde'
        ): 
            # Solo permitir que el vehículo circule si el semáforo está verde
            vehiculo['estado'] = 'circula'

    # Incrementar el tiempo
    tiempo_actual += 1

# Visualización de los resultados
# plt.figure(figsize=(12, 6))
# plt.plot(datos_tiempo, datos_vehiculos, label='Número de vehículos en circulación')
# plt.xlabel('Tiempo')
# plt.ylabel('Número de vehículos')
# plt.title('Simulación del Flujo de Tráfico')
# plt.legend()
# plt.grid(True)
# plt.show()