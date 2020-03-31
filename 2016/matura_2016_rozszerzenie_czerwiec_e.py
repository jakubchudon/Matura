plik = open('/Users/jakubchudon/Desktop/matury/2016_rozszerzenie_czerwiec/liczby.txt', 'r')
max_dec=0
min_dec=10000000000000
for linia in plik:
    linia=linia.strip()
    liczba=linia[0:len(linia)-1]
    sys=int(linia[len(linia)-1])
    wynik=int(liczba,sys)
    if wynik>max_dec:
        max_dec=wynik
        max_kod=linia
    if wynik<min_dec:
        min_dec=wynik
        min_kod=linia
print(min_kod,min_dec)
print(max_kod,max_dec)