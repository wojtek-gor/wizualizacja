# zad1
# filmy = ['Królestwo Niebieskie', 'Duże dzieci', 'Siedmu gniewnych ludzi', 'Cast Away', 'Jestem bogiem',
#          'Krzyrzacy']
# filmy.reverse()
# filmy.insert(5, 'Potwory i spółka')
# filmy.insert(5, 'Pingwiny z magadaskaru')
# filmy.insert(5, 'Psy')
# filmy.insert(5, 'Patriota')
# zad 2
# filmy = {1: 'Krzyrzacy', 2: 'Jestem bogiem', 3: 'Cast Away', 4: 'Siedmu gniewnych ludzi', 5: 'Duże dzieci',
#          6: 'Patriota', 7: 'Psy', 8: 'Pingwiny z magadaskaru', 9: 'Potwory i spółka', 10: 'Królestwo Niebieskie'}
# zad3
# przedmioty = {'CAD': 'komputerowe wspomaganie projektowania', 'PS': 'programowanie strukturalne', 'ANG': 'angielski',
#               'WD': 'wizualizacja danych', 'MD': 'matematyka dyskretna',
#               'AMDI': 'analiza matematyczna dla informatyków', 'PO': 'przedmiot ogólnouczelniany'}
# licznik=0
# while licznik<=przedmioty.__len__():
#     licznik+=1
# print(licznik-1)
# zad4
# a = input("Podaj liczbe:")
# a = float(a)
# a = a ** a
# print(a)
# zad5
# a=input("Wpisz napis")
# print(a.count('a'))
# zad6
# a = input("Podaj liczbe:")
# b = input("Podaj liczbe:")
# c = input("Podaj liczbe:")
# a = int(a)
# b = int(b)
# c = int(c)
# if a%2==0 and b>c:
#     print("Ok")
# else:
#     print("Nie")
# zad7
# liczby = [3, 4, 4.5, 64, 5.66, 6.71, 4]
# liczba = liczby[-1]
# for i in liczby:
#     print(liczba+i)
#     liczba = i
# zad8
# liczby = []
# i=0
# while i<10:
#     a = input("Podaj liczbe:")
#     a = float(a)
#     if a%2==0:
#         liczby = liczby+[a]
#     i+=1
# print(liczby)
# zad9
lista=[1, 2, 3, 4, 5, 6]
for i in lista:
    if i==1 or i==6:
        print("OOOOOO")
    else:
        print("O    O")
