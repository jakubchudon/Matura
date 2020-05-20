plik=open("C:/matura/2013/dane.txt")
wynik=0
for linia in plik:
    linia=linia.strip()
    dl=len(linia)-1
    x=linia[0]
    y=linia[dl]
    if x==y:
        wynik+=1
print(wynik)



