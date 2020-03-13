plik=open('/Users/jakubchudon/Desktop/2018_PR/DANE_PP/liczby.txt')
max=0
for linia in plik:
    linia=int(linia.strip())
    if linia%2==0 and linia>max:
        max=linia
print(max)