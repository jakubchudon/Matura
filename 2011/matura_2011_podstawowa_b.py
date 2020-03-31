plik=open('/Users/jakubchudon/Desktop/matury/2011_podstawa/hasla.txt')
for linia in plik:
    linia=str(linia.strip())
    if linia== linia[::-1]:
        print(linia)