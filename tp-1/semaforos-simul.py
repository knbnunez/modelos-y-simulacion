import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
tiempo_simulacion       = 200  # Tiempo total de la simulación en unidades arbitrarias
ciclo_semaforo_verde    = 30
ciclo_semaforo_amarillo = 5
ciclo_semaforo_rojo     = 10
ciclo_semaforo          = ciclo_semaforo_verde + ciclo_semaforo_amarillo + ciclo_semaforo_rojo # Duración del ciclo de un semáforo
#
num_semaforos           = 4
ciclo_semaforos         = ciclo_semaforo * num_semaforos # Duración total de 1 ciclo completo
#
num_vehiculos_inicial   = 25
tiempo_llegada_vehiculos= 15  # Tiempo promedio entre llegadas de vehículos

# Inicializa variables
tiempo_actual           = 0
vehiculos               = []  # Lista para almacenar la posición, estado y origen/destino de los vehículos


# Función para actualizar el estado de los semáforos
def actualizar_estado_semaforos(tiempo_actual):
    tiempo_actual_ciclo             = tiempo_actual % ciclo_semaforos # Momento actual dentro del ciclo (0 hasta ciclo_semaforos)
    tiempo_actual_ciclo_semaforo    = tiempo_actual_ciclo % ciclo_semaforo # Momento actual dentro del ciclo de un semaforo (0 hasta ciclo_semaforo)
    semaforo_actual                 = (tiempo_actual_ciclo // ciclo_semaforo) % num_semaforos # Determina el semaforo que debe ser utilizado en el momento actual del ciclo completo
    
    # Determina el estado del semáforo actual basado en el ciclo actual
    estados = ['rojo'] * num_semaforos # Crea un array de 4 (num_semaforos) ['rojo', 'rojo', 'rojo', 'rojo']
    if tiempo_actual_ciclo_semaforo   < ciclo_semaforo_verde:                             estados[semaforo_actual] = 'verde'
    elif tiempo_actual_ciclo_semaforo < ciclo_semaforo_verde + ciclo_semaforo_amarillo: estados[semaforo_actual] = 'amarillo'
    else:                                                                               estados[semaforo_actual] = 'rojo'
    
    return estados

# Función para generar vehículos
def generar_vehiculos(tiempo_actual, num_vehiculos):
    for _ in range(num_vehiculos):
        origen = np.random.choice(['A', 'B', 'C', 'D'])
        destino = np.random.choice(['A', 'B', 'C', 'D'])
        while destino == origen:  # Asegurarse de que el destino es diferente del origen
            destino = np.random.choice(['A', 'B', 'C', 'D'])
        llegada = tiempo_actual + np.random.uniform(0, tiempo_llegada_vehiculos)
        vehiculos.append({'tiempo_llegada': llegada, 'estado': 'espera', 'origen': origen, 'destino': destino})

# Inicialización de la simulación
generar_vehiculos(0, num_vehiculos_inicial)

# Almacenar datos para la visualización
tiempos = []
cant_vehiculos_circulando = []

# Simulación
while tiempo_actual < tiempo_simulacion:
    # Actualizar el estado de los semáforos
    semaforo_A, semaforo_B, semaforo_C, semaforo_D = actualizar_estado_semaforos(tiempo_actual)
    
    # Actualizar vehículos
    for vehiculo in vehiculos:
        if vehiculo['estado'] == 'espera' and vehiculo['tiempo_llegada'] <= tiempo_actual:
            origen = vehiculo['origen']
            destino = vehiculo['destino']
            
            if   origen == 'A' and semaforo_A == 'verde': vehiculo['estado'] = 'circula'
            elif origen == 'B' and semaforo_B == 'verde': vehiculo['estado'] = 'circula'
            elif origen == 'C' and semaforo_C == 'verde': vehiculo['estado'] = 'circula'
            elif origen == 'D' and semaforo_D == 'verde': vehiculo['estado'] = 'circula'

    
    # Contar vehículos en circulación
    num_vehiculos_circulando = sum(1 for v in vehiculos if v['estado'] == 'circula')
    tiempos.append(tiempo_actual)
    cant_vehiculos_circulando.append(num_vehiculos_circulando)
    
    # Incrementar el tiempo
    tiempo_actual += 1
