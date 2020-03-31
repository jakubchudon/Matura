def suma_cyfr(liczba):
    zmienna=liczba
    suma=0
    while zmienna>0:
        cyfra=zmienna%10
        suma+=cyfra
        zmienna=zmienna//10
    else:return suma
plik=open('/Users/jakubchudon/Desktop/2018_PR/DANE_PP/liczby.txt')
tablica=[]
for linia in plik:
    linia=linia.strip()
    tablica.append(int(linia))
    if suma_cyfr(int(linia))>30:
        print(linia)
x=list(map(suma_cyfr,tablica))
print('\n')
print(sum(x))


