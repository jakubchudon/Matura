w=0
plik=open('/Users/jakubchudon/Desktop/matury/2015_rozszerzenie_maj/liczby.txt')
for linia in plik:
    linia=linia.strip()
    zera=linia.count("0")
    jedynki=linia.count("1")
    if zera>jedynki:
        w+=1
print(w)