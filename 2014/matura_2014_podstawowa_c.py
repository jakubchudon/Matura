plik=(open('/Users/jakubchudon/Desktop/matury/2014_podstawa/Pary_liczb.txt'))
wynik=0
def suma_cyfr(liczba):
    zmienna=liczba
    suma=0
    while zmienna>0:
        cyfra=zmienna%10
        suma+=cyfra
        zmienna=zmienna//10
    else:
        return suma
for linia in plik:
    linia=linia.split()
    x=int(linia[0])
    y=int(linia[1])
    suma_x=suma_cyfr(x)
    suma_y=suma_cyfr(y)
    if suma_x==suma_y:
        wynik+=1
print(wynik)