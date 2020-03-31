plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2015_maj/liczby.txt')
odp=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2015_maj/odp_4.1.txt','w')
w=0
for lina in plik:
    linia=lina.strip()
    zera=lina.count("0")
    jedynki=lina.count("1")
    if zera>jedynki:
        w+=1
print(w)
odp.write(str(w))