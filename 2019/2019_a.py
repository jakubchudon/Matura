plik=open('/Users/jakubchudon/Desktop/2019_PR/Dane_PP2/dane.txt')
kobieta=0
mezczyzna=0
for linia in plik:
    linia=linia.strip()
    dl=len(linia)-2
    x=linia[dl]
    if int(linia[dl])%2==0:
        kobieta+=1
    else:mezczyzna+=1
print(kobieta,mezczyzna)
