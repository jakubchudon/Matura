plik=open('/Users/jakubchudon/Desktop/matury/2016_podstawa/dane4.txt')
from funkcje import read_linia
tablica=[]
for linia in plik:
    linia=read_linia(linia)
    tablica.append(linia)
for x in range(0,2000):
    for i in range(2,tablica[x]):
        if tablica[x]%i==0:
            break
    else:
        for z in range(2,tablica[x+1]):
            if tablica[x+1]%z==0:
                break
        else:
            if tablica[x]+2==tablica[x+1] or tablica[x+1]+2==tablica[x]:
                print(tablica[x],tablica[x+1])


