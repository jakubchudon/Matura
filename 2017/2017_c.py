plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/dane.txt")
odp=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/odp_6.3.txt",'w')
kontrastujace=0
tablica=[]
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    rzad=[]
    for x in linia:
        rzad.append(int(x))
    tablica.append(rzad)
for y in range(len(tablica)):
    for x in range(len(tablica[0])):
        kontrast = False
        #lewy
        if x>0:
            r=abs(tablica[y][x]-tablica[y][x-1])
            if r>128:
                kontrast=True
        #prawy
        if x<319:
            r=abs(tablica[y][x]-tablica[y][x+1])
            if r>128:
                kontrast=True
        #gora
        if y>0:
            r=abs(tablica[y][x]-tablica[y-1][x])
            if r>128:
                kontrast=True
        #dol
        if y<199:
            r = abs(tablica[y][x] - tablica[y+1][x])
            if r > 128:
                kontrast = True
        #sprawdzenie
        if kontrast==True:
            kontrastujace+=1
print(kontrastujace)
odp.write(str(kontrastujace))



