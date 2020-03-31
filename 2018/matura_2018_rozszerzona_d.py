dane1=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/przyklad1.txt')
dane2=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/przyklad2.txt')
wynik_d=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/wynik_d.txt','w')
wiersz3=[]
for linia1 in dane1:
    plik1 = []
    linia1=linia1.split()
    for x in range(len(linia1)):
        plik1.append(int(linia1[x]))
    else:
        for linia2 in dane2:
            plik2 = []
            linia2=linia2.split()
            for y in range(len(linia2)):
                plik2.append(int(linia2[y]))
            else:
                wiersz3 = []
                i=0
                while i<=20:
                    if len(plik1)==0:
                        for y in range(len(plik2)):
                            wiersz3.append(plik2[y])
                        break
                    if len(plik2)==0:
                        for y in range(len(plik1)):
                            wiersz3.append(plik1[y])
                        break
                    else:
                        if plik1[0]<=plik2[0]  :
                            wiersz3.append(plik1[0])
                            plik1.pop(0)
                            i=+1
                        else:
                            plik2[0]<=plik1[0]
                            wiersz3.append(plik2[0])
                            plik2.pop(0)
                            i=+1
                for i in range(len(wiersz3)):
                    if i==len(wiersz3)-1:
                        wynik_d.write(str(wiersz3[i]))
                    else:
                        wynik_d.write(str(wiersz3[i])+',')
                else:
                    wynik_d.write('\n')
                    break





