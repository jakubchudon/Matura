plik=open('/Users/jakubchudon/Desktop/matury/2013_podstawa/napisy.txt')
tablica=[]
for linia in plik:
    linia=linia.strip()
    tablica.append(len(linia))
for i in range(2,16+1):
    print(i,tablica.count(i))