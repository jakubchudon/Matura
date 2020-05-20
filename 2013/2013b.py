plik=open("C:/matura/2013/dane.txt")
wynik=0
for linia in plik:
    linia=linia.strip()
    dec=str(int(linia,8))
    if dec[0]==dec[len(dec)-1]:
        wynik+=1
print(wynik)