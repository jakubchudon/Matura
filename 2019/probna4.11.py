plik=open("C:/Users/Jakub/Desktop/probna/dane4.txt")
maksimum=0
tab=[]
for linia in plik:
    linia=linia.strip()
    linia=int(linia)
    tab.append(linia)
max=0
min=2**11
for x in range(len(tab)-1):
    roznica=abs(tab[x]-tab[x+1])
    if roznica>max:
        max=roznica
    if roznica<min:
        min=roznica
print(max)
print(min)
