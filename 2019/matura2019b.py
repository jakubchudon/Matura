liczby = open('/Users/jakubchudon/Desktop/matura2019/pierwsze.txt')
tablica=[]
for linia in liczby:
    liczba1=linia.split()
    liczba=int(liczba1[0])
    odwrotna=int(str(liczba)[::-1])
    tablica.append(odwrotna)
for x in tablica:
    for dzielnik in range(2,x):
        if x% dzielnik ==0:
            break
    else:
        print(str(x)[::-1])



