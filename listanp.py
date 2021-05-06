import numpy as np
# Zad1
# a = np.arange(20)
# a = a*4
# print(a)
# Zad2
# a = [2.3,4.2,7.6,1.0,22.3,5.2,6.3]
# b = np.fromiter(a, dtype='int32')
# print(b)
# Zad3
# def macierz(n):
#     tab = np.arange(n*n)
#     tab = tab.reshape((n,n))
#     tab = 2**tab
#     return tab
# print(macierz(5))
# Zad4
# def generuj(podstaw, ilosc):
#     a = np.logspace(1, ilosc, ilosc, base=podstawa, dtype='int32')
#     return a
# print(generuj(2,6))
# Zad5
# def wektor(n):
#     mat = np.diag([2**x for x in range(n)], 2)
#     return mat
# print(wektor(3))

# Zad9
# a = np.arange(25).reshape((5,5))
# a = (2+a)*3
# print(a)