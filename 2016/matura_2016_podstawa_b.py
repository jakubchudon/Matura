plik=open('/Users/jakubchudon/Desktop/matury/2016_podstawa/dane4.txt')
max=0
min=3000
for linia in plik:
    linia=linia.split()
    linia=int(linia[0])
    for i in range(2,linia//2):
        if linia%i==0:
            break
    else:
        if linia>max:
            max=linia
        if linia<min:
            min=linia
print(max,min)