plik=open('/Users/jakubchudon/Desktop/matury/2013_podstawa/napisy.txt')
wynik=0
for linia in plik:
    linia=linia.strip()
    if len(linia)%2==0:
        wynik+=1
print(wynik)
