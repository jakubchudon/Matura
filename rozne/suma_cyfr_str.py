liczba = input("podaj liczbe\n")
liczba1 = str(liczba)
dlugosc=len(liczba1)
i=0
tablica=[]
for i in range(0,dlugosc):
    cyfra=int(liczba1[i])
    tablica.append(cyfra)
print(sum(tablica))
