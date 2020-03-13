plik = open('/Users/jakubchudon/Desktop/matury/2016_rozszerzenie_czerwiec/liczby.txt', 'r')
suma = 0
for linia in plik:
    linia=linia.strip()
    liczba=(linia[0:len(linia)-1])
    dl=len(liczba)-1
    if linia.endswith('8'):
        for i in liczba:
            i=int(i)
            suma+=(i*(8**dl))
            dl=dl-1
print(suma)