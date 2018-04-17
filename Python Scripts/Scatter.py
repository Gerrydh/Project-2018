"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

filename = ("master.kkids.obslist")

data = np.loadtxt(filename,skiprows=14,dtype=str)

x = data[:,7]
y = data[:,8]
u = data[:,18]
v = data[:,19]
z = data[:,20]

x1 = x.astype(float)
y1 = y.astype(float)

plt.scatter(x,y)
plt.savefig('hi.png')


import numpy as np
import matplotlib.pyplot as plt

filename = ("master.kkids.obslist")

data = np.loadtxt(filename,skiprows=14,dtype=str)

x = data[:,7]
y = data[:,8]
u = data[:,18]
v = data[:,19]
z = data[:,20]

x1 = x.astype(float)
y1 = y.astype(float)

plt.scatter(x,y)
plt.savefig('hi.png')
