plik=open('/Users/jakubchudon/Desktop/2019_PR/Dane_PP2/dane.txt')
listopad=0
for linia in plik:
    linia=linia.strip()
    x=(linia[2:4])
    if x=='11' or x=='31':
        listopad+=1
print(listopad)
