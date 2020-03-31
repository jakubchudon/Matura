from funkcje import suuma_cyfr
plik=open('/Users/jakubchudon/Desktop/dane.txt')
wynik=0
for linia in plik:
    linia=linia.strip()
    if linia==linia[::-1]:
        wynik+=suuma_cyfr(int(linia))