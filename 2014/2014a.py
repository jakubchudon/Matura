plik=open("C://matura/2014/NAPIS.TXT")
wynik=0
for linia in plik:
    linia=linia.strip()
    suma_kodow=0
    for i in range(len(linia)):
        x=ord(linia[i])
        suma_kodow+=x
    for dzielnik in range(2,suma_kodow//2):
        if suma_kodow%dzielnik==0:
            break
    else:
        wynik+=1
print(wynik)

