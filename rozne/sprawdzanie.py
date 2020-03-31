odp=open('/Users/jakubchudon//Desktop/matury/2016_rozszerzenie_maj/wynik_6.1.txt')
odp1=open('/Users/jakubchudon//Desktop/matury/2016_rozszerzenie_maj/wynik_6.1.1.txt')
od=[]
od1=[]
w=0
for linia in odp:
    linia=linia.strip()
    od.append(linia)
    w+=1
print(w)
for linia1 in odp1:
    linia1=linia1.strip()
    od1.append(linia1)
w=0
for i in range(len(od)):
    if od[i]==od1[i]:
        print(w,"tak")
        w+=1
    else:
        print(w,"nie")
        w+=1

