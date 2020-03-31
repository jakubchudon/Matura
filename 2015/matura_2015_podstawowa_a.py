plik=open('/Users/jakubchudon/Desktop/matury/2015_podstawa/slowa.txt')
dl=[]
for linia in plik:
    dl.append(len(linia.strip()))
for i in range(1,13):
    print(i,dl.count(i))

