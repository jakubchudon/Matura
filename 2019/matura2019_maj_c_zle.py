liczby=[]
plik=open('/Users/jakubchudon/Desktop/matura2019/Dane_PR/przyklad.txt')
for linia in plik:
    linia1=int(linia.strip())
    liczby.append(linia1)
i0=0
r=1
nwd=0
for z in range(0,len(liczby)-1):
    const=liczby[z]
    x = liczby[z]
    y = liczby[(z+1)]
    while r!=0:
        if x%y==0:
            nwd=y
            if nwd >1:
                print(const)
                break
            else:
                break
        else:
            r=x%y
            zmienna=x
            x=y
            y=r


