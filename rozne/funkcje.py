import math
def suuma_cyfr(cyfra):
    zmienna_liczba = cyfra
    suma_cyfr = 0
    while zmienna_liczba > 0:
        cyfra = zmienna_liczba % 10
        suma_cyfr += cyfra
        zmienna_liczba = zmienna_liczba // 10
    else:
        return suma_cyfr
def suma_silnia(cyfra):
    zmienna_liczba = cyfra
    suma_cyfr = 0
    while zmienna_liczba > 0:
        cyfra = zmienna_liczba % 10
        suma_cyfr += math.factorial(cyfra)
        zmienna_liczba = zmienna_liczba // 10
    else:
        return suma_cyfr

def nwd(a,b):
    while int(a)%int(b) !=0:
        r=a%b
        a=b
        b=r
    return b
def pierwsza(liczba):
    x=1
    for dzielnik in range(2, liczba):
        if liczba % dzielnik == 0:
            break
    else:
        return x
def read_linia(linia):
    linia = linia.split()
    linia = int(linia[0])
    return linia
def parzysta(x):
    parzyste=0
    for i in range(len(x)):
        y=int(x[i])
        if y%2==0:
            parzyste+=1
    return parzyste
def nieparzysta(x):
    nieparzyste=0
    for i in range(len(x)):
        y=int(x[i])
        if y%2!=0:
            nieparzyste+=1
    return nieparzyste
