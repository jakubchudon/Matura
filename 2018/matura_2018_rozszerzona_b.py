from funkcje import parzysta,nieparzysta
dane1=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/dane1.txt')
dane2=open('/Users/jakubchudon/Desktop/matury/2018_rozszerzona/dane2.txt')
wynik=0
for linia1 in dane1:
    linia1=linia1.split()
    parzyste =parzysta(linia1)
    nieparzyste =nieparzysta(linia1)
    for linia2 in dane2:
       linia2 = linia2.split()
       parzyste1 =parzysta(linia2)
       nieparzyste2 =nieparzysta(linia2)
       if parzyste1 == 5 and nieparzyste2 == 5 and parzyste==5 and nieparzyste==5:
           wynik+=1
       break
print(wynik)
