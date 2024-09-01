import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
tiempo_simulacion       = 1800  # Tiempo total de la simulación en unidades arbitrarias
ciclo_semaforo_verde    = 30
ciclo_semaforo_amarillo = 5
num_semaforos           = 4

# El ciclo total de un semáforo sigue siendo el mismo
ciclo_semaforo = ciclo_semaforo_verde + ciclo_semaforo_amarillo

# Calculamos el tiempo de rojo como el tiempo en el que los otros semáforos están en verde o amarillo
ciclo_semaforo_rojo = (num_semaforos - 1) * ciclo_semaforo  # Rojo ahora es dinámico

# Recalcula el ciclo total de todos los semáforos
ciclo_semaforos = ciclo_semaforo * num_semaforos

num_vehiculos_inicial   = 200

# Datos para la recolección de eventos
tiempo_espera_total = { 'A': [], 'B': [], 'C': [], 'D': [] }
cantidad_vehiculos_verde = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }
vehiculos_esperando_rojo = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }
max_vehiculos_esperando_rojo = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }
total_vehiculos_origen = { 'A': 0, 'B': 0, 'C': 0, 'D': 0 }  # Nueva variable para contar los vehículos por origen
contador_ciclos = 0

tiempo_actual           = 0
vehiculos               = []  # Lista para almacenar la posición, estado y origen/destino de los vehículos


# Función para actualizar el estado de los semáforos
def actualizar_estado_semaforos(tiempo_actual):
    tiempo_actual_ciclo             = tiempo_actual % ciclo_semaforos
    tiempo_actual_ciclo_semaforo    = tiempo_actual_ciclo % ciclo_semaforo
    semaforo_actual                 = (tiempo_actual_ciclo // ciclo_semaforo) % num_semaforos
    
    estados = ['rojo'] * num_semaforos
    if tiempo_actual_ciclo_semaforo   < ciclo_semaforo_verde:
        estados[semaforo_actual] = 'verde'
    elif tiempo_actual_ciclo_semaforo < ciclo_semaforo_verde + ciclo_semaforo_amarillo:
        estados[semaforo_actual] = 'amarillo'
    
    return estados

# Función para generar vehículos
def generar_vehiculos(tiempo_actual, num_vehiculos):
    for _ in range(num_vehiculos):
        origen = np.random.choice(['A', 'B', 'C', 'D'])
        destino = np.random.choice(['A', 'B', 'C', 'D'])
        while destino == origen:
            destino = np.random.choice(['A', 'B', 'C', 'D'])
        llegada = tiempo_actual + np.random.uniform(0, tiempo_simulacion)
        vehiculos.append({'tiempo_llegada': llegada, 'estado': 'espera', 'origen': origen, 'destino': destino})
        total_vehiculos_origen[origen] += 1

# Función para actualizar el estado de los vehículos
def actualizar_estado_vehiculos(tiempo_actual, estados_semaforos):
    vehiculos_esperando_en_rojo = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for vehiculo in vehiculos:
        if vehiculo['estado'] == 'espera' and vehiculo['tiempo_llegada'] <= tiempo_actual:
            origen = vehiculo['origen']
            semaforo_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
            estado_semaforo = estados_semaforos[semaforo_index[origen]]
            
            if estado_semaforo == 'verde':
                vehiculo['estado'] = 'circula'
                cantidad_vehiculos_verde[origen] += 1
                tiempo_espera = tiempo_actual - vehiculo['tiempo_llegada']
                tiempo_espera_total[origen].append(tiempo_espera)
            else:
                vehiculos_esperando_en_rojo[origen] += 1

    return vehiculos_esperando_en_rojo

# Función para actualizar la cantidad máxima de vehículos esperando en rojo
def actualizar_max_vehiculos_esperando_rojo(vehiculos_esperando_en_rojo):
    for semaforo in ['A', 'B', 'C', 'D']:
        if vehiculos_esperando_en_rojo[semaforo] > max_vehiculos_esperando_rojo[semaforo]:
            max_vehiculos_esperando_rojo[semaforo] = vehiculos_esperando_en_rojo[semaforo]

# Función para calcular los resultados
def calcular_resultados():
    tiempo_promedio_espera = { semaforo: np.mean(tiempo_espera_total[semaforo]) if tiempo_espera_total[semaforo] else 0 for semaforo in ['A', 'B', 'C', 'D'] }
    cantidad_total_vehiculos_verde = { semaforo: cantidad_vehiculos_verde[semaforo] for semaforo in ['A', 'B', 'C', 'D'] }
    cantidad_promedio_vehiculos_verde = { semaforo: cantidad_total_vehiculos_verde[semaforo] / contador_ciclos if contador_ciclos else 0 for semaforo in ['A', 'B', 'C', 'D'] }

    print("Tiempo promedio de espera (por semáforo):")
    for semaforo, promedio in tiempo_promedio_espera.items():
        print(f"Semáforo {semaforo}: {promedio:.2f}")

    print("\nCantidad promedio de vehículos que pasan en verde (por semáforo):")
    for semaforo, promedio in cantidad_promedio_vehiculos_verde.items():
        print(f"Semáforo {semaforo}: {promedio:.2f}")

    print("\nMayor cantidad de autos esperando en rojo (por semáforo):")
    for semaforo, max_esperando in max_vehiculos_esperando_rojo.items():
        print(f"Semáforo {semaforo}: {max_esperando}")

    print("\nCantidad total de autos por origen:")
    for semaforo, total in total_vehiculos_origen.items():
        print(f"Semáforo {semaforo}: {total}")

# Inicialización de la simulación
generar_vehiculos(0, num_vehiculos_inicial)

# Simulación
while tiempo_actual < tiempo_simulacion:
    estados_semaforos = actualizar_estado_semaforos(tiempo_actual)
    vehiculos_esperando_en_rojo = actualizar_estado_vehiculos(tiempo_actual, estados_semaforos)
    actualizar_max_vehiculos_esperando_rojo(vehiculos_esperando_en_rojo)

    # Incrementar el tiempo
    tiempo_actual += 1

    # Contar ciclos completados
    if tiempo_actual % ciclo_semaforos == 0:
        contador_ciclos += 1

# Calcular y mostrar resultados
calcular_resultados()
