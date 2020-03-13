plik = open('/Users/jakubchudon/Desktop/pliki/hasla.txt')
for linia in plik:
    wyraz=linia.split()
    zmienna = wyraz[0]
    dlugosc=len(zmienna)
    for x in range(0, (dlugosc-1)):
        a=x
        b=x+1
        if ord(zmienna[a])+ord(zmienna[b])==220:
            print(zmienna)
            break





