#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.sin(x))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('tight')
plt.show()
