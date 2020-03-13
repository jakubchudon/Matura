plik=open('/Users/jakubchudon/Desktop/matury/2016_rozszerzenie_czerwiec/liczby.txt','r')
wynik=0
for linia in plik:
    linia=linia.strip()
    if linia.endswith("8"):
        wynik+=1
print(wynik)
wynik=0
for linia in plik:
    linia=linia.strip()
    if linia.endswith("4") and linia.count("0")==0:
        wynik+=1
print(wynik)