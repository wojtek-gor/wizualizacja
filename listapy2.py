import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
# Do zadania od 1 do 3
# tab = pd.ExcelFile('datasets/imiona.xlsx')
# tab = pd.read_excel(tab)

# zad1
# tab = tab.groupby(['Rok']).agg({'Liczba':['sum']})
# tab.plot()
# plt.show()
# zad2
# tab = tab.groupby(['Plec']).agg({'Liczba':['sum']})
# print(tab)
# wykres = tab.plot.bar()
# wykres.set_ylabel("Milionów")
# plt.show()
# zad3
# tab = tab[(tab.Rok >= 2013)].groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = tab.plot.pie(subplots=True,autopct='%.1f%%')
# plt.show()
# zad4
tab = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
tab = tab.groupby('Sprzedawca').agg({'Utarg':['count']})
print(tab)
wyk = tab.plot.bar()
wyk.set_ylabel('Ilość zamówień')
wyk.set_xlabel('Sprzedawcy')
wyk.legend()
plt.show()