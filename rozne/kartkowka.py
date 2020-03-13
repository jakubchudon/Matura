import random
liczby=[]
parzyste=[]
suma_cyfr=[]
suma_parzyste=[]
i = 0
l=100
while i <= l:
    liczby.append(random.randint(0,1000))
    i = i + 1
i=0
for i in liczby:
    if i % 2 ==0:
        parzyste.append(i)
print(parzyste)
for liczba in parzyste:
    liczba1=liczba
    suma = 0
    while liczba1 >0:
        cyfra = liczba1% 10
        suma += cyfra
        liczba1 = liczba1//10
    else:
        suma_cyfr.append(suma)
print(suma_cyfr)
for liczba_suma in suma_cyfr:
    if liczba_suma % 2 ==0:
        suma_parzyste.append(liczba_suma)
print(suma_parzyste)

