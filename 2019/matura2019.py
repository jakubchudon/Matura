liczby = open('/Users/jakubchudon/Desktop/matura2019/liczby.txt')
tablica=[]
for linia in liczby:
    liczba1=linia.split()
    liczba=int(liczba1[0])
    tablica.append(liczba)
for x in tablica:
    if x in range(100,5000):
        for dzielnik in range(2,x):
            if x% dzielnik ==0:
                break
        else:
            print(x)



