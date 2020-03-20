plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2019_maj/liczby.txt')
potegi=[]
w=0
x=0
wynik=0
while x <100000:
    x=3**w
    potegi.append(x)
    w+=1
for linia in plik:
    if int(linia.strip()) in potegi:
        wynik+=1
print(wynik)
