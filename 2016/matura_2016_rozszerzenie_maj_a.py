plik=open('/Users/jakubchudon//Desktop/matury/2016_rozszerzenie_maj/dane_6_1.txt')
odp=open('/Users/jakubchudon//Desktop/matury/2016_rozszerzenie_maj/wynik_6.1.1.txt','w')
k=107%26
for linia in plik:
    linia=linia.strip()
    dl=len(linia)
    tekst=""
    for i in range(dl):
        asci=ord(linia[i])
        if asci+ k > 90:
            x = 65 + (90-asci)
        else:
            x=asci+3
        x=chr(x)
        tekst+=x
    else:
        odp.write(tekst)
        odp.write("\n")

