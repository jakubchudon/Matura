plik = open('/Users/jakubchudon/Desktop/pliki/dane.txt')
wynik = open('/Users/jakubchudon/Desktop/pliki/wynik.txt','w')
for linia in plik:
    wyraz=linia.split()
    zmienna = wyraz[0]
    pali = (str(zmienna))[::-1]
    if pali==str(zmienna):
        wynik.write(wyraz[0])
        wynik.write('\n')
        print(wyraz[0],'\t')
