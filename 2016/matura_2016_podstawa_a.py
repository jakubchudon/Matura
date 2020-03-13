plik=open('/Users/jakubchudon/Desktop/matury/2016_podstawa/dane4.txt')
zapis=open('/Users/jakubchudon/Desktop/matury/2016_podstawa/dane4_wynik1.txt','w')
wynik=0
for linia in plik:
    linia=linia.split()
    linia=int(linia[0])
    for i in range(2,linia//2):
        if linia%i==0:
            break
    else:
        #zapis.write(str(linia))
        #zapis.write(str('\n'))
        wynik=wynik+1
print(wynik)
zapis.write(str(wynik))