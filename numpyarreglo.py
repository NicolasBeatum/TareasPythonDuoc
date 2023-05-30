import numpy as np
import random as rd

arreglo = np.array([rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100),rd.randint(0, 100)])
print(arreglo)

arreglo_mayor = arreglo[:].copy()
print(arreglo_mayor.max())

arreglo_menor = arreglo[:].copy()
print(arreglo_menor.min())

arreglo_suma = arreglo[:].copy()
print(arreglo_suma.sum())

arreglo_prom = arreglo[:].copy()
print(arreglo_prom.mean())

print(arreglo)
    