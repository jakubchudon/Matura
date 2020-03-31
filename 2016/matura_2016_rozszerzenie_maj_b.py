plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2016_maj/dane_6_2.txt')
odp=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2016_maj/odp_6.2.txt','w')
for linia in plik:
    linia=linia.split()
    if len(linia)==2:
        kod=int(linia[1])
        k=kod%26
        linia=linia[0]
        dl=len(linia)
        tekst=""
        for i in range(dl):
            k = kod % 26
            asci=ord(linia[i])
            if asci- k < 65:
                k=k+((asci-k)-asci)
                x=90-k
            else:
                x=asci-k
            x=chr(x)
            tekst+=x
        else:
            odp.write(tekst)
            odp.write("\n")