plik=open('/Users/jakubchudon//Desktop/matury/2016_rozszerzenie_maj/dane_6_3.txt')
odp=open('/Users/jakubchudon//Desktop/matury/2016_rozszerzenie_maj/wynik_6.3.txt','w')
for linia in plik:
    linia=linia.split()
    linia_p=(linia[1])
    # k=kod%26
    linia=linia[0]
    dl=len(linia)
    tekst=""
    n=0
    k=[]
    for i in range(len(linia)):
        if ord(linia_p[i])-ord(linia[i])<0:
            w=26+ord(linia_p[i])-ord(linia[i])
        else:
            w=ord(linia_p[i])-ord(linia[i])
        k.append(w)
    else:
        for i in range(len(k)-1):
            if k[i]!=k[i+1]:
                print(linia)
                odp.write(linia)
                odp.write("\n")
                break