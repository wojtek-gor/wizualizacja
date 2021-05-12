import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

# zad1
# y = [1/y for y in range(1, 21)]
# x = [x for x in range(1, 21)]
# plt.plot(x, y)
# plt.show()
# zad2
# y = [1/y for y in range(1, 21)]
# x = [x for x in range(1, 21)]
# plt.plot(x, y, 'g>:', label='f(x)=1/x')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title("Wykres funkcji f(x)=1/x")
# plt.show()
# zad3
# lista = np.arange(0, 30, 0.1)
# sin = np.sin(lista)
# cos = np.cos(lista)
# plt.plot(lista, sin, label='sin(x)')
# plt.plot(lista, cos, 'r', label='cos(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('sin(x) i cos(x)')
# plt.title("Wykres sin(x) i cos(x)")
# plt.show()
# zad4
# lista = np.arange(0, 30, 0.1)
# sin1 = np.sin(lista*(-1))
# sin2 = np.sin(lista)+2
# plt.plot(lista, sin1, 'orange', label='sin(x)')
# plt.plot(lista, sin2, label='sin(x)')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title("Wykres sin(x), sin(x)")
# plt.show()
# zad7
# dz = pd.read_csv('datasets/zamowienia.csv', delimiter=';')
# grupa = dz.groupby(['Sprzedawca']).size()
# wykres = grupa.plot.pie(subplots=True, autopct='%.f %%', fontsize=20, explode=[0, 0.1, 0, 0.4, 0, 0, 0, 0.3, 0],
#                         shadow=True)
# plt.show()