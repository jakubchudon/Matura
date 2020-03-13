def print2d(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i][j], end=' ')
        print(' ')
tablica2d=[]
tab=[]
for i in range(1,11):
    for j in range(1,11):
        tab.append(i*j)
    tablica2d.append(tab)
    tab=[]
print2d(tablica2d)
