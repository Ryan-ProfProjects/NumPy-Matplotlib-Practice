import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)

xv, yv = np.meshgrid(x, y)

f = lambda x,y: np.sin(5*x) * np.cos(5*y)/5 * np.exp(x)
z = f(xv, yv)

ax = plt.subplot(projection="3d")
ax.plot_surface(xv, yv, z, cmap="viridis")
plt.show()   