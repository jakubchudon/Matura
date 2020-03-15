plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/dane.txt")
jasny=0
ciemny=265
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    for x in linia:
        if int(x)>jasny:
            jasny=int(x)
        if int(x)<ciemny:
            ciemny=int(x)
print(jasny,ciemny)