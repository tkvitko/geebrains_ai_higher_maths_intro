#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(1.1*x))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
