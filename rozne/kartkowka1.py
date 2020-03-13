import random
liczby=[]
i = 0
l=10
for i in range(0,l):
    liczby.append(random.randint(0,1000))
print(liczby)
for liczba in liczby:
    if liczba % 2 ==0:
        liczba1 = liczba
        suma = 0
        while liczba1>0:
            cyfra = liczba1 % 10
            suma += cyfra
            liczba1 = liczba1 // 10
        else:
            if suma%2==0:
                print(liczba)


