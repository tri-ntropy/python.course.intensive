import numpy as np
import matplotlib.pyplot as plt

def euler(t0, tf, x0, v0, n, fuerza = lambda x, v, i: 0):
    """
    Esta es una función de simulación que sigue el algoritmo de Euler
    Parametros
    ----------
    
    """
    tiempo, paso_tiempo = np.linspace(t0, tf, n + 1, retstep = True)

    velocidad = np.zeros(n + 1)
    desplazamiento = np.zeros(n + 1)

    velocidad[0] = v0
    desplazamiento[0] = x0

    for i in range(1, n + 1):
        velocidad[i] = velocidad[i - 1] + paso_tiempo * fuerza(desplazamiento, velocidad, i)
        desplazamiento[i] = desplazamiento[i - 1] + paso_tiempo * velocidad[i]

    return {"x" : desplazamiento,
            "v" : velocidad,
            "t" : tiempo,
            "dt" : paso_tiempo}


def graficar_desplazamiento(t, x):
    plt.figure(figsize = (6, 2.5))
    plt.plot(t, x)
    plt.ylabel("$x(t)$")
    plt.xlabel("$t$")
    plt.show()

def graficar_velocidad(t, v):
    plt.figure(figsize = (6, 2.5))
    plt.plot(t, v)
    plt.ylabel("$v(t)$")
    plt.xlabel("$t$")
    plt.show()