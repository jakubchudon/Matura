plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/dane.txt")
wynik=0
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    if list(linia)!=list(reversed(linia)):
        wynik+=1
print(wynik)
