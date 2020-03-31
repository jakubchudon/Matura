dane1=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/dane1.txt')
dane2=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/dane2.txt')
wiersze=[]
nrwiersza=1
wynik=0
for linia1 in dane1:
    plik1 = []
    linia1=linia1.split()
    for x in range(len(linia1)):
        plik1.append(linia1[x])
    else:
        for linia2 in dane2:
            plik2 = []
            linia2=linia2.split()
            for y in range(len(linia2)):
                plik2.append(linia2[y])
            else:
                i=1
                while True and i<=9:
                    if  plik1[i] in plik2:
                        i+=1
                    else:
                        nrwiersza+=1
                        break
                else:
                    wynik+=1
                    wiersze.append(nrwiersza)
                    nrwiersza+=1
                break
print(wynik,wiersze)

