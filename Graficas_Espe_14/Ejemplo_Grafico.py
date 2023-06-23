### Ejercicio Basico de Graficacion
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.bar([1, 2, 3], [3, 2, 1])
plt.show()

fig, ax= plt.subplots()
ax.pie([5,4,3,2,1])
plt.show()

fig, ax= plt.subplots()
x=np.random.random([16,16])
ax.imshow(x)
plt.show()