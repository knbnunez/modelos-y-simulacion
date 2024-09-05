# Escalón: x(t) = A ⋅ μ (t − t0) / μ (t − t0) = (0 => t < t0) : (1 => t >= t0)
# Según lo que investigué, la función Escalón se utiliza para representar el cambio de tensión en un instante de tiempo, junto a la intensidad de activación

# import numpy as np
import matplotlib.pyplot as plt

def escalon(A, t, t0):
    return A * (1 if t >= t0 else 0) # Operador ternario

A   = float(input(f"\nIngrese la intesidad de la señal A: "))
t   = int(input(f"Ingrese el intervalo de tiempo t: "))
t0  = float(input(f"Ingrese el instánte de tiempo donde se activa la señal t0: "))


t           = [i for i in range(0, t+1)]      # Tiempo en X
activacion  = [escalon(A, i, t0) for i in t]  # Valor de y a partir de t0

# Graficar la señal
plt.plot(t, activacion, label=f'x(t) = {A}·μ(t - {t0})')
plt.axvline(x=t0, color='r', linestyle='--', label=f't0 = {t0}')  # Marcar el t0
plt.title('Señal Escalón x(t)')
plt.xlabel('Tiempo t')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()