plik=open('/Users/jakubchudon/Desktop/2019_PR/Dane_PP2/dane.txt')
tab=[1,3,7,9,1,3,7,9,1,3,1]
for linia in plik:
    linia=linia.strip()
    y=0
    suma=0
    for i in tab:
        x=i*int(linia[y])
        suma+=x
        y=y+1
    else:
        if suma%10!=0:
            print(linia)
