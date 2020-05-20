plik=open("C://matura/2014/NAPIS.TXT")
wynik=0
for linia in plik:
    linia=linia.strip()
    kod=0
    zmienna=0
    for i in range(len(linia)):
        x=ord(linia[i])
        if x<=kod:
            break
        else:
            kod = x
            zmienna+=1
    if zmienna==len(linia):
        print(linia)