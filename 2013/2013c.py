plik=open("C:/matura/2013/dane.txt")
wynik=0
min=524289
max=0
for linia in plik:
    linia=linia.strip()
    dl=len(linia)
    for i in range(0,dl-1):
        if linia[i]>linia[i+1]:
            break
    else:
        wynik+=1
        dec =int(linia, 8)
        if dec>max:
            max=dec
        if dec<min:
            min=dec
print(wynik,min,max)
