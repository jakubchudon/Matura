plik=open('/Users/jakubchudon/Desktop/2018_PR/DANE_PP/liczby.txt')
for linia in plik:
    linia=linia.strip()
    if linia==linia[::-1]:
        print(linia)