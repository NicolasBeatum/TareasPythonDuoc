import numpy as np
valor = np.arange(1, 103, dtype=object)
asientos = np.reshape(valor, (34,3))
print(asientos)

print(asientos[0,0])
