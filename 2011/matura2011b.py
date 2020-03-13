plik = open('/Users/jakubchudon/Desktop/pliki/hasla.txt')
for linia in plik:
    wyraz=linia.split()
    zmienna = wyraz[0]
    pali = (str(zmienna))[::-1]
    if pali==str(zmienna):
        print(wyraz[0],'\t')
