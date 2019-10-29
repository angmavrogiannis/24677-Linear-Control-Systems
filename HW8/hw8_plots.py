import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

#code for plotting the phase portrait
w = 10
y, x = np.mgrid[-w:w:100j, -w:w:100j]
x_dot = y
y_dot = np.zeros(x.shape)
plt.streamplot(x, y, x_dot, y_dot)
plt.show()

#code for plotting the derivative of the energy function
#with respect to x_1 and x_2
x1 = np.linspace(-1, 1, 1000)
x2 = np.linspace(-1, 1, 1000)
x1, x2 = np.meshgrid(x1, x2)
v = -4 * np.multiply(x1**4, x2**2)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(x1, x2, v)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$\dot{V}$')
plt.show()