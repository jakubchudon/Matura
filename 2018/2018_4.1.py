plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2018_maj/sygnaly.txt")
zapis=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2018_maj/wynik_4.1.txt",'w')
tablica=[]
for linia in plik:
    linia=linia.strip()
    tablica.append(linia)
print(tablica)
i=39
tekst=''
while i <1000:
    x=tablica[i]
    x=x[9]
    tekst+=x
    i+=40
print(tekst)
zapis.write(tekst)
