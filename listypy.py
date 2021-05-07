import numpy as np
import pandas as pd
import xlrd
import openpyxl
# zad1
# imiona = pd.ExcelFile('datasets/imiona.xlsx')
# tab = pd.read_excel(imiona, header=0)
# zad2
# print(tab[(tab.Liczba < 1000)])

# print(tab[(tab.Imie == 'WOJCIECH')])

# print(tab.groupby(['Rok']).agg({'Liczba':['sum']}))

# a=tab[(tab.Rok >= 2005)  & (tab.Rok <= 2010)]
# print(a.agg({'Liczba':['sum']}))

# a = tab[(tab.Rok == 2000) & (tab.Plec == 'M')]
# a = a.agg({'Liczba':['sum']})
# print(a)

# print(tab.sort_values('Liczba',ascending=False).groupby(['Plec']).nth(0))
# zad3
tab = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
# print(tab)
# print(tab['Sprzedawca'].unique())

# a = tab['Utarg'].sort_values(ascending=False)
# print(a[0:5])

# print(tab.groupby(['Sprzedawca']).agg({'Utarg':['count']}))

# print(tab.groupby(['Kraj']).agg({'Utarg':['sum']}))

# print(tab[((tab['Data zamowienia']>='2005-01-01') & (tab['Data zamowienia'] <= '2005-12-31') & (tab.Kraj == 'Polska'))]\
#     .agg({'Utarg':['sum']}))

# print(tab[(tab['Data zamowienia'] >= '2004-01-01') & (tab['Data zamowienia'] <= '2004-12-31')].agg({'Utarg':['mean']}))

