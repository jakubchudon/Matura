plik=open('/Users/jakubchudon/Desktop/matury/2010_podstawa/dane.txt')
wynik=open('/Users/jakubchudon/Desktop/matury/2010_podstawa/wynik.txt','w')
for linia in plik:
    linia=str(linia.strip())
    if linia==linia[::-1]:
            print(linia)
            wynik.write(linia)
            wynik.write('\n')