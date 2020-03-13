import math
plik=open('/Users/jakubchudon/Desktop/matury/2016_rozszerzenie_maj/punkty.txt')
wn=0
for linia in plik:
    linia=linia.split()
    x=int(linia[0])
    y=int(linia[1])
    r=math.sqrt((((x-200)**2)+((y-200)**2)))
    if r==200:
        print(x,y)
    elif r<200:
       wn+=1
print(wn)