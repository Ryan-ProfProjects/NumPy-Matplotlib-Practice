import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 1000)
y = np.linspace(0, 1, 1000)

def f(x, y): return x*np.cos(x) + y*np.sin(y)

X, Y = np.meshgrid(x, y)

z = f(X, Y)

ax = plt.subplot(projection = "3d")
ax.plot_surface(X, Y, z)
plt.show()