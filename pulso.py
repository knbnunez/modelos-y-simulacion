# Función Pulso: p(t) = A.[µ(t −to)−µ(t −to−D)]

import matplotlib.pyplot as plt
from math import exp, sin, pi
import numpy as np

'''
Explicación de términos:

funciona como la función Escalón y representa además la "bajada" de tensión con "µ(t −to−D)".
'''


def mu(t, t0):
    return 1 if t >= t0 else 0

def pulso(A, t, t0, D):
    return A * (mu(t, t0) - mu(t, t0 + D))

print("\n --- Señal Pulso --- \n")
A   = float(input("Amplitud de la señal A: "))
t0  = float(input("Tiempo de inicio del pulso t0 (en segundos): "))
D   = float(input("Duración del pulso D (en segundos): "))
t   = float(input("Tiempo final de la señal t (en segundos): "))

cant_puntos = 1000 # se podría consultar por consola
# Definir el intervalo de tiempo (por ejemplo, de 0 a t en 1000 puntos)
t_values = np.linspace(0, t, cant_puntos)  # Genera n puntos de tiempo entre 0 y t

# Calcular el valor de la señal Pulso para cada valor de tiempo
x_values = [pulso(A, ti, t0, D) for ti in t_values]

# Graficar la señal
plt.plot(t_values, x_values, label=f'p(t) = {A}·[μ(t - {t0}) - μ(t - {t0} - {D})]')
plt.title('Pulso Rectangular p(t)')
plt.xlabel('Tiempo t')
plt.ylabel('p(t)')
plt.legend()
plt.grid(True)
plt.show()
