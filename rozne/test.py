















tablica1=[[2,6],[6,2],[8,2],[5,12]]
tab = [[1 for col in range(5)] for row in range(10)]
tablica=[]
# for i in range(1,201):
#     print(i)
plik=open('/Users/jakubchudon/Downloads/Dane_PR/dane.txt')
for linia in plik:
    linia=linia.split()
    for wiersz in range(1,201):
        tb = []
        index = 0
        for kolumna in range(1,321):
            tb.append(wiersz)
            tb.append(kolumna)
            tb.append(int(linia[index]))
            tablica.append(tb)
            tb=[]
            index+=1
print(tablica)