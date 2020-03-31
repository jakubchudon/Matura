import math
plik=open('/Users/jakubchudon/Desktop/matury/2016_rozszerzenie_maj/punkty.txt')
pkt_kola=0
pkt_kwadratu=0
for linia in plik:
    linia=linia.split()
    x=int(linia[0])
    y=int(linia[1])
    r=math.sqrt((((x-200)**2)+((y-200)**2)))
    if r<=200:
        pkt_kola+=1
    if r>200:
        pkt_kwadratu+=1
else:
    x=(pkt_kola/pkt_kwadratu)
    pi=x/(200*200)
print(pi)