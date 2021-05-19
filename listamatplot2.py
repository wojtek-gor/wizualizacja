import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter
np.random.seed(151629)
# zad1
# wyk = plt.figure()
# osie = wyk.gca(projection='3d')
# a = np.linspace(0, 2*np.pi,100)
# z=a
# x=np.sin(a)
# y=2*np.cos(a)
# osie.plot(x,y,z)
# plt.show()
# zad2
# def los(n, vmin, vmax):
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
# wyk = plt.figure()
# osie = wyk.add_subplot(projection='3d')
# n=200
# for c, m, dol, gora in [('r', 'o', -10, 20), ('b','.', -20, 10),('y','^',0, 20),('orange','*',-20,-10),('black','D',-20,20)]:
#     x=los(n,13,100)
#     y=los(n, 2, 50)
#     z=los(n, dol, gora)
#     osie.scatter(x,y,z, c=c, marker=m)
# plt.show()
# zad3
# wyk = plt.figure()
# osie = wyk.gca(projection='3d')
# x = np.arange(-5,5,0.25)
# y = np.arange(-5,5,0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2 + y**2)
# z = np.sin(r)
# pow = osie.plot_surface(x,y,z,cmap=plt.get_cmap('Accent'),linewidth=0,antialiased=False)
# pow1 = osie.plot_surface(x,y,z,cmap=plt.get_cmap('Blues'),linewidth=0,antialiased=False)
# pow2 = osie.plot_surface(x,y,z,cmap=plt.get_cmap('Pastel1'),linewidth=0,antialiased=False)
# pow3 = osie.plot_surface(x,y,z,cmap=plt.get_cmap('binary'),linewidth=0,antialiased=False)
# pow4 = osie.plot_surface(x,y,z,cmap=plt.get_cmap('brg'),linewidth=0,antialiased=False)
# plt.show()
