slowo=open("C:/matura/2012/sz.txt")
klucz=open("C:/matura/2012/klucze2.txt")
slowa=[]
klucze=[]
for linia in slowo:
    slowa.append(linia.strip())
for linia in klucz:
    klucze.append(linia.strip())
for i in range(len(slowa)):
    wyraz=slowa[i]
    kod=klucze[i]
    while len(wyraz)>len(kod):
        kod=kod+kod
    tekst_zaszyfrowany=""
    for p in range(len(wyraz)):
        zmienna=0
        x=ord(wyraz[p])-(ord(kod[p])-64)
        while x<65:
            x=x+26
        tekst_zaszyfrowany+=chr(x)
    print(tekst_zaszyfrowany)

