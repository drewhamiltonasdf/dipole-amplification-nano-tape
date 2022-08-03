from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import plotly.figure_factory as ff

m = [1, 1, 1]   #i, j, k

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(-0.5, 2, 0.2),
                      np.arange(-0.5, 2, 0.2),
                      np.arange(-0.5, 2, 0.2))

u = (3*x*(x+y+z)) / (x**2 + y**2 + z**2)**(5/2) - (1 / ((x**2+y**2+z**2)**(3/2)))
v = (3*y*(x+y+z)) / (x**2 + y**2 + z**2)**(5/2) - (1 / ((x**2+y**2+z**2)**(3/2)))
w = (3*z*(x+y+z)) / (x**2 + y**2 + z**2)**(5/2) - (1 / ((x**2+y**2+z**2)**(3/2)))

#u = (z - y) / ((x**2+y**2+z**2)**(3/2))
#v = (x - z) / ((x**2+y**2+z**2)**(3/2))
#w = (y - x) / ((x**2+y**2+z**2)**(3/2))


# Color by 1 over magnitude
c = 1 / (np.sqrt(u**2+v**2+w**2))
# Flatten and normalize
c = (c.ravel() - c.min()) / c.ptp()
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))
# Colormap
c = plt.cm.hsv(c)

#ax.quiver(x, y, z, u, v, w, length=0.1)
ax.quiver(x, y, z, u, v, w,length=0.1, normalize=True, color=c)

plt.show()