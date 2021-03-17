import random
# Zad1
# a = [1-x for x in range(1,11)]
# print(a)
# b = [4**x for x in range(8)]
# print(b)
# c = [x for x in b if x%2==0]
# print(c)
# Zad2
# lista1 = []
# for x in range(11):
#     lista1.append(int(random.random()*10+1))
# listap = [x for x in lista1 if x % 2 == 0]
# print(lista1)
# print(listap)
# Zad3
# lista = {'chleb': 'sztuki', 'bułki': 'sztuki', 'marchewka': 'kilogramy', 'kurczak': 'kilogramy',
#          'mleko': 'litry'}
# lista2 = {x for x in lista if lista[x] == 'sztuki'}
# print(lista)
# print(lista2)
# Zad4
# def prosty(przyprostokatna1,przyprostokatna2,przeciwprostokatna):
#     if(przyprostokatna1**2+przyprostokatna2**2==przeciwprostokatna**2):
#         print('Trójkąt prostokątny.')
#     else:
#         print('To nie jest trójkąt prostokątny.')
# prosty(3, 4, 5)
# prosty(2, 3, 5)
# Zad5
# def trapez(a=1, b=1, h=1):
#     return ((a+b)*h)/2
# print(trapez())
# print(trapez(2, 4, 5))
# Zad6
# def iloczyn(a=1, b=4, ile=10):
#     wynik = a
#     for x in range(a,a+ile+1):
#         wynik=wynik*b
#     return wynik
# print(iloczyn(2,6,6))
# Zad7
# def iloczyn(*liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         wynik=1
#         for x in liczby:
#             wynik=wynik*x
#         return wynik
#
# print(iloczyn(2,6,6,7,8,9,4))
# Zad8
# def zakupy(**lista):
#     print("Ilość produktów to: ")
#     print(len(lista))
#     suma = 0
#     for x in lista:
#         suma+=lista[x]
#     print("Wartość produktów to: ")
#     print(suma)
#
# zakupy(chleb=3.5, bułka=0.5, jajko=0.3, woda=1)