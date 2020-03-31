plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2016_maj/dane_6_1.txt')
odp=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2016_maj/odp_6.1.txt','w')
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
        print(tekst)
        odp.write(tekst)
        odp.write("\n")

