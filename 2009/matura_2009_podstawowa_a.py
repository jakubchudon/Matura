plik=open('/Users/jakubchudon/Desktop/matury/2009_podstawa/liczby.txt')
pierwsze=[]
for x in range(2,1000):
    for dzielnik in range(2,x):
        if x% dzielnik ==0:
            break
    else:
            pierwsze.append(x)
for linia in plik:
    linia=int(linia.strip())
    for i in range(0,len(pierwsze)):
        if linia==pierwsze[i]**2:
            print(linia)
            break
            edit