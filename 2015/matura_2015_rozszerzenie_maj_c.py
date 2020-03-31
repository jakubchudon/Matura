min=2**250
max=0
index=1
min_index=0
max_index=0
plik=open('/Users/jakubchudon/Desktop/matury/2015_rozszerzenie_maj/liczby.txt')
for linia in plik:
    linia=linia.strip()
    linia=int(linia,2)
    if linia>max:
        max=linia
        max_index=index
    if linia<min:
        min=linia
        min_index=index
    index+=1
print(min_index,min)
print(max_index,max)