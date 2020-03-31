from funkcje import suuma_cyfr
liczby = open('/Users/jakubchudon/Desktop/matura2019/pierwsze.txt')
tablica=[]
wynik=0
for linia in liczby:
    liczba1=linia.split()
    liczba=int(liczba1[0])
    tablica.append(liczba)
for x in tablica:
    w=x
    while w>=9:
        w=suuma_cyfr(w)
    else:
        if w==1:
            wynik=wynik+1
print(wynik)
