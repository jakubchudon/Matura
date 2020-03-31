plik=open('/Users/jakubchudon/Desktop/matury/2011_podstawa/hasla.txt')
parzysta=0
nieparzysta=0
for linia in plik:
    linia=linia.strip()
    if len(linia)%2==0:
        parzysta+=1
    else: nieparzysta+=1
print('parzyste:',parzysta)
print('nieparzyste:',nieparzysta)