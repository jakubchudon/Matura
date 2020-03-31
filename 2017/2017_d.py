plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/dane.txt")
odp=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/odp_6.4.txt",'w')
max_kolumna=[]
tablica=[]
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    rzad=[]
    for x in linia:
        rzad.append(int(x))
    tablica.append(rzad)
for x in range(len(tablica[0])):
    wynik_wiersza=1
    max_wiersza=0
    for y in range(len(tablica)-1):
        if tablica[y][x]==tablica[y+1][x]:
            wynik_wiersza+=1
            if wynik_wiersza>max_wiersza:
                max_wiersza=wynik_wiersza
        else:
            wynik_wiersza=1
    else:
        max_kolumna.append(max_wiersza)
print(max(max_kolumna))
odp.write(str(max(max_kolumna)))

