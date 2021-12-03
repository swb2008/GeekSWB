from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def nixushu(n: int):
    return int(str(n)[::-1])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(0, 1000, 10)
Y = list(map(lambda i: ((i - nixushu(i)) / 9), X))
#Z = list(map(lambda j: ((j - nixushu(j)) / 9), X))
Z = list(map(lambda j: ((j - nixushu(j)) / 9), X))#np.sin(-X*Y)
#ax.plot_wireframe(X, Y, Z)
ax.plot_trisurf(X, Y, Z, linewidth=0.2, antialiased=True)
# plt.plot(x, y)
plt.show()
