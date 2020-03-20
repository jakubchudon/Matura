def suma_silnia(liczba):
    import math
    wynik=0
    liczba=str(liczba)
    for i in range(len(liczba)):
        wynik+=math.factorial(int(liczba[i]))
    else:
        return wynik
plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2019_maj/liczby.txt')
for linia in plik:
    linia=int(linia.strip())
    if linia==suma_silnia(linia):
        print(linia)
