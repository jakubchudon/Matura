plik=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzenie/sygnaly.txt')
slowa=[]
nowe_slowo=[]
for linia in plik:
    linia=linia.strip()
    slowa.append(linia)
i=39
while i<=1000:
    x=slowa[i]
    nowe_slowo.append(x[9])
    i+=40
    print(x[9])
