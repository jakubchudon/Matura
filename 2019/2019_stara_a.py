plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2019_stara_maj/dzialki.txt')
wynik=0
trawa=0
for linia in plik:
    linia=linia.strip()
    if linia!="":
        wiersz=[]
        for i in range(len(linia)):
            wiersz.append(linia[i])
        trawa+=wiersz.count("*")
    else:
        if trawa>=(0.7*30*30):
            wynik+=1
        trawa = 0
print(wynik)
