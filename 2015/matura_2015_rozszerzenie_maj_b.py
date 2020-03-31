w2=0
w8=0
plik=open('/Users/jakubchudon/Desktop/matury/2015_rozszerzenie_maj/liczby.txt')
for linia in plik:
    linia=linia.strip()
    linia=int(linia,2)
    if linia%2==0:
        w2+=1
    if linia%8==0:
        w8+=1
print(w2,w8)