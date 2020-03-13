plik=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzenie/sygnaly.txt')
odp=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzenie/odp.txt','w')
for linia in plik:
    linia=linia.strip()
    dl=len(linia)
    ascii_max=0
    ascii_min=90
    for x in range(dl):
        if ord(linia[x])>ascii_max:
            ascii_max=ord(linia[x])
        if ord(linia[x])<ascii_min:
            ascii_min=ord(linia[x])
    else:
        if ascii_max-ascii_min<=10:
            odp.write(linia)
            odp.write('\n')