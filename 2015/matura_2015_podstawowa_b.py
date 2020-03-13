slowa=open('/Users/jakubchudon/Desktop/matury/2015_podstawa/slowa.txt')
nowe=open('/Users/jakubchudon/Desktop/matury/2015_podstawa/nowe.txt')
slowa1=[]
for slowo in slowa:
    slowo=slowo.strip()
    slowa1.append(slowo)
for linia in nowe:
    wynik=0
    lustro=0
    linia=linia.strip()
    for i in range(0,1000):
        pali=slowa1[i]
        if linia == slowa1[i]:
            wynik=wynik+1
        if linia==pali[::-1]:
            lustro+=1
    print(linia,wynik,lustro)
