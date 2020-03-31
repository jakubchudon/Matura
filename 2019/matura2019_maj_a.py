plik=open('/Users/jakubchudon/Desktop/matura2019/Dane_PR/liczby.txt')
x=plik.readlines()
plik.close()
t=[]
i=0
while True:
    p=3**i
    t.append(p)
    if p>100000:
        break
    i+=1
wynik=0
for a in x:
    y=a
    a=int(a.strip())
    if a in t:
        wynik+=1
        print(a)
#print(wynik)