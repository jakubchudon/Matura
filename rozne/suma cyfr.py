liczba = int(input('Podaj liczbe\n'))
zmienna_liczba = liczba
suma_cyfr= 0
while zmienna_liczba >0:
    cyfra = zmienna_liczba % 10
    suma_cyfr += cyfra
    zmienna_liczba = zmienna_liczba//10
else:
    print(suma_cyfr)