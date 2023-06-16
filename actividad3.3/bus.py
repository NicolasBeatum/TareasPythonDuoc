import numpy as np

valor = np.arange(1, 101, dtype=object)
asientos = np.reshape(valor, (10,10))
print(asientos)

num= int(input("Ingrese un asiento: "))
for f in range(10):
    for c in range(10):
        if num == asientos[f,c]:
            print(f"Su asiento es: {num}")
            asientos[f,c] = "X"
print(asientos)
