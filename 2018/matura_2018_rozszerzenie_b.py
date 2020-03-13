plik=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzenie/przyklad.txt')
dl=0
for linia in plik:
    linia=linia.strip()
    unikalne_litery=[]
    for i in linia:
        if not i in unikalne_litery:
            unikalne_litery.append(i)
    else:
        if len(unikalne_litery)>dl:
            dl=len(unikalne_litery)
            slowo=linia
print(slowo,dl)


