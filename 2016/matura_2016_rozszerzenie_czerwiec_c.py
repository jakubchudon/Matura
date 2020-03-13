plik = open('/Users/jakubchudon/Desktop/matury/2016_rozszerzenie_czerwiec/liczby.txt', 'r')
wynik = 0
for linia in plik:
    linia=linia.strip()
    if linia.endswith("2") and (int(linia[0:len(linia)-1]))%2==0:
        wynik+=1
print(wynik)