# Zad1
# plik = open("liczby.txt", "a+")
# lista = [x*2 for x in range(31)]
# lista = str(lista)
# plik.write(lista)
# plik.close()

# Zad2
# plik = open("liczby.txt", "r+")
# liczby = plik.readline()
# plik.close()
# print(liczby)

# Zad3
# with open("liczby.txt", "a+") as plik:
#     for linia in range(11):
#         napis = str(linia) + "\n"
#         plik.write(napis)
#
#
# with open("liczby.txt", "r") as plik2:
#     for znak in plik2:
#         print(znak, end="")

# Zad4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miar, cena_jed):
#         self.nazwa_produktu=nazwa_produktu
#         self.ilosc= ilosc
#         self.jednostka_miary=jednostka_miar
#         self.cena_jed=cena_jed
#     def wyswietl_produkt(self):
#         print("{} {}zl/{}".format(self.nazwa_produktu, self.cena_jed, self.jednostka_miary))
#     def ile_produktu(self):
#         print("{} {}".format(self.ilosc, self.jednostka_miary))
#     def ile_kosztuje(self):
#         a = self.ilosc*self.cena_jed
#         return a
#
# wydruk = NaZakupy("Kurczak", 0.5, "kg", 24)
# print(wydruk)
# wydruk.wyswietl_produkt()
# wydruk.ile_produktu()
# print(wydruk.ile_kosztuje())

# Zad5
