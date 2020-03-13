dane1=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/dane1.txt')
dane2=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/dane2.txt')
tablica1=[]
tablica2=[]
wynik=0
for linia1 in dane1:
    linia1=linia1.strip()
    linia1=linia1.split(" ")
    x=len(linia1)-1
    tablica1.append(linia1[x])
for linia2 in dane2:
    linia2=linia2.strip()
    linia2=linia2.split(" ")
    x=len(linia2)-1
    tablica2.append(linia2[x])
for i in range(1000):
    if tablica1[i]==tablica2[i]:
        wynik+=1
print(wynik)