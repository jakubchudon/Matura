plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2015_maj/liczby.txt')
odp=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2015_maj/odp_4.3.txt','w')
nr_wiersza=1
tablica=[]
for linia in plik:
    tab=[]
    linia=linia.strip()
    liczba=int(linia,2)
    tab.append(liczba)
    tab.append(nr_wiersza)
    tablica.append(tab)
    nr_wiersza+=1
najwieksza=max(tablica)[1]
najmniejsza=min(tablica)[1]
print(najmniejsza)
print(najwieksza)
odp.write("numer wiersza zawierającego minimalną liczbę: "+ str(najmniejsza)+"\n")
odp.write("numer wiersza zawierającego maksymalna liczbę: "+ str(najwieksza)+"\n")
