plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2018_maj/sygnaly.txt")
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
