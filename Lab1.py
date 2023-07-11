"""
Lab #1

Ale Gómez
Tío Pedro Arriola

"""


import random as rd
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import skew

# Ejercicio 1 - Distribución de probabilidad
def Ejercicio1():
    # Definición de constantes
    mean = 0
    std = 1
    sample = 1000

    # Generación de datos
    datos = np.random.normal(mean, std, sample)

    # Cálculo de estadísticas
    datosMedia = np.mean(datos)
    datosVar = np.var(datos)
    datosAsimetria = skew(datos)

    # Impresión de resultados
    print("Media: ", datosMedia)
    print("Varianza: ", datosVar)
    print("Asimetría: ", datosAsimetria)

    # Gráfica de histograma
    sns.histplot(datos, kde=True)
    plt.show()


Ejercicio1()
