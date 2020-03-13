plik = open('/Users/jakubchudon/Desktop/pliki/hasla.txt')
parzyste=0
nieparzyste=0
for linia in plik:
    wyraz=linia.split()
    zmienna = wyraz[0]
    x=len(zmienna)
    if x%2 == 0:
        parzyste=parzyste+1
    else:
        nieparzyste=nieparzyste+1
print(parzyste,nieparzyste)