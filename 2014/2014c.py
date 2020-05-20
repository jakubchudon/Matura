plik=open("C://matura/2014/NAPIS.TXT")
tablica=[]
for linia in plik:
    linia=linia.strip()
    tablica.append(linia)
dl=len(tablica)
for slowo in tablica:
    if tablica.count(slowo)>1:
        print(slowo)
        tablica.remove(slowo)

