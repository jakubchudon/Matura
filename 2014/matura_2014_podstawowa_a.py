plik=(open('/Users/jakubchudon/Desktop/matury/2014_podstawa/Pary_liczb.txt'))
wynik=0
for linia in plik:
    linia=linia.split()
    x=int(linia[0])
    y=int(linia[1])
    if x%y==0 or y%x==0:
        wynik+=1
print(wynik)
