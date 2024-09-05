# Función Seno: x(t) = A . sen(2 . π . fo . t + θ)

import matplotlib.pyplot as plt
from math import sin, pi


'''
Explicación de términos:

x(t):   es el valor de la onda en un momento dado. 
        Sería como medir cuánto sube o cuánto baja en distintos momentos de reloj.

A:      controla la amplitud de la onda.

sen:    es la función trigonométrica :p .

2π:     describe la relación entre la circunferencia y el diámetro.
        En este caso 2π representa un ciclo completo de la función seno (corresponde a una oscilación completa de la señal).

fo:     representa la cantidad de ciclos (oscilaciones completas) ocurren en un segundo. Hz

t:      es el intervalo de tiempo observado en segundos.

θ:      es el desplazamiento (en el tiempo) respecto a la posición inicial de la onda.
        Es como si adelantáramos o retrasáramos el ciclo (dependiendo del valor).
'''

def seno(A, fo, ti, θ):
    return A * sin(2 * pi * fo * ti + θ)

print("\n --- Función Seno --- \n")
print("\nIngrese por favor:")
A   = float(input("Amplitud de la señal A: "))
fo  = float(input("Cantidad de ciclos por segundo fo (en Hertz): "))
t   = int(input("Tiempo final t (en segundos): ")) # Debería poder ser FLOAT, OJO
θ   = float(input("Desplazamiento del ciclo θ (en radianes): "))

# Intervalo de tiempo de la función
#t_values = [i for i in range(t)] # REVISAR, lo simplifiqué, no normalicé
t_values = [i for i in range(t)]

# Calcular la señal seno para cada instante de tiempo ti
x_values = [seno(A, fo, ti, θ) for ti in t_values]


# Graficar la señal
plt.plot(t_values, x_values, label=f'x(t) = {A}·sin(2π·{fo}·t + {θ})')
plt.title('Señal Senoidal x(t)')
plt.xlabel('Tiempo t (s)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()
