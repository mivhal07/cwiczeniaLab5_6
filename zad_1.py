import math

import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(1, 20)
# y = 1 / x
# plt.plot(x, y, 'bo-', label='liniowa')
# plt.xlabel('etykieta osi x')
# plt.ylabel('etykieta osi y')
# plt.title('Wykres jednej linii')
# plt.show()

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y, 'bp-', label='liniowa')
plt.xlabel('etykieta osi x')
plt.ylabel('etykieta osi y')
plt.title('Wykres jednej linii')
plt.show()