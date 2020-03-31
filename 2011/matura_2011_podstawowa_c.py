plik=open('/Users/jakubchudon/Desktop/matury/2011_podstawa/hasla.txt')
wynik=open('/Users/jakubchudon/Desktop/matury/2011_podstawa/wynik_c.txt','w')
for linia in plik:
    linia=str(linia.strip())
    dl=len(linia)-1
    for i in range(0,dl):
        if ord(linia[i])+ord(linia[i+1])==220:
            print(linia)
            wynik.write(linia)
            wynik.write('\n')