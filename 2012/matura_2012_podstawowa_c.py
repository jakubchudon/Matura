plik=open('/Users/jakubchudon/Desktop/matury/2012_podstawa/cyfry.txt')
wynik=0
for linia in plik:
    tablica=[]
    linia=str(linia.strip())
    dl=len(linia)
    for x in range(0, dl - 1):
        if linia[x] < linia[x + 1] and linia[x] != linia[x + 1]:
            wynik = linia
        else:
            break
    else:print(wynik)

