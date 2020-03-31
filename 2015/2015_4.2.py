plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2015_maj/liczby.txt')
odp=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2015_maj/odp_4.2.txt','w')
p2=0
p8=0
for lina in plik:
    linia=int(lina.strip(),2)
    if linia%2==0:
        p2+=1
    if linia%8==0:
        p8+=1
print(p2,p8)
odp.write("podzielne przez 2: "+str(p2)+'\n')
odp.write("podzielne przez 8: "+str(p8)+'\n')