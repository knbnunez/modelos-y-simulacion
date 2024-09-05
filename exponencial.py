# Función Exponencial: x(t) = A.e^α(t−t0)

import matplotlib.pyplot as plt
from math import exp
import numpy as np

'''
Explicación de términos:

x(t):   es el valor de la onda en un momento dado. 
        Sería como medir cuánto sube o cuánto baja en distintos momentos de reloj.

A:      es la amplitud inicial.

e:      es una constante (un nro irracional) que se usa para calcular el crecimiento o decrecimiento.

α:      es la tasa de de crecimiento (>0) o decrecimiento (<0).

(t-t0): determina cuándo cambia el valor de la función (+ o -).
'''

def exponencial(A, α, t, t0):
    return A * exp(α * (t - t0))

print("\n --- Función Seno --- \n")
print("\nIngrese por favor:")
A   = float(input("Amplitud inicial A: "))
α   = float(input("Tasa de crecimiento o decrecimiento α: "))
t0  = float(input("Instante de tiempo t0: "))
t   = float(input("Tiempo final en segundos t: "))

# Intervalo de tiempo de la función
t_values = np.linspace(0, t, 1000)  # Genera un arreglo de 1000 posiciones con valores entre 0 y t

# Calcular la señal exponencial para cada instante ti
x_values = [exponencial(A, α, ti, t0) for ti in t_values]


# Graficar la señal
plt.plot(t_values, x_values, label=f'x(t) = {A}·e^({α}·(t - {t0}))')
plt.title('Señal Exponencial x(t)')
plt.xlabel('Tiempo t (s)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()
