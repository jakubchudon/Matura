import random
tablica=[]
i = 0
l=5
for i in range(l):
    tablica.append(random.randint(0,1000))
print(tablica)
index=0
for x in tablica:
    for dzielnik in range(2,x):
        if x% dzielnik ==0:
            break
        else:
            liczba1=x
            suma=0
            while liczba1>0:
                cyfra = liczba1 % 10
                suma += cyfra
                liczba1 = liczba1 // 10
            else:
                for suma in range(2,suma):
                    if suma% dzielnik ==0:
                        break
                else:
                     print(x)
                     break