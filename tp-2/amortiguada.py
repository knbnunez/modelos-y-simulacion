# Función Amortiguada: x(t) = A.sen(2.π.f0.t +θ).e^α.t

import matplotlib.pyplot as plt
from math import exp, sin, pi
import numpy as np

'''
Explicación de términos:

funciona como una combinación de la función seno + la función exponencial

El término: A.sen(2.π.f0.t +θ) funciona igual que en seno.
El término: e^α.t funciona similar como en exponencial, define la velocidad con la que cambia la función seno.
'''

def senal_amortiguada(A, f0, θ, α, ti):
    return A * sin(2 * pi * f0 * ti + θ) * exp(α * t)

print("\n --- Señal Amortiguada --- \n")
A   = float(input("Amplitud de la señal A: "))
f0  = float(input("Frecuencia de la señal f0 (ciclos por segundo): "))
θ   = float(input("Desplazamiento del ciclo θ: "))
α   = float(input("Tasa de cambio α: "))
t   = float(input("Tiempo final t (en segundos): "))

# Definir el intervalo de tiempo
t_values = np.linspace(0, t, 1000)  # Genera un arreglo de 1000 posiciones con valores entre 0 y t

# Calcular el valor de la señal amortiguada para cada valor de tiempo
x_values = [senal_amortiguada(A, f0, θ, α, ti) for ti in t_values]

# Graficar la señal
plt.plot(t_values, x_values, label=f'x(t) = {A}·sin(2π·{f0}·t + {θ})·e^({α}·t)')
plt.title('Señal Amortiguada x(t)')
plt.xlabel('Tiempo t (s)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()
