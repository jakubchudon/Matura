from funkcje import suuma_cyfr
plik=open('/Users/jakubchudon/Desktop/matura2019/Cyfry.txt')
wynik_a=0
for linia in plik:
    linia1=int(linia.strip())
    if linia1%2==0:
        wynik_a+=1
print(wynik_a)
for linia in plik:
    linia1=int(linia.strip())
    suma=suuma_cyfr(linia1)
    liczba=linia1



