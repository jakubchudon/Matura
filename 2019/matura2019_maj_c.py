from funkcje import nwd
liczby=[]
plik=open('/Users/jakubchudon/Desktop/matura2019/Dane_PR/liczby.txt')
for linia in plik:
    linia1=int(linia.strip())
    liczby.append(linia1)
N=len(liczby)
dzielmax=0
dlmax=0
pierwszamax=0
for j in range(N-1):
    dl = 1
    pierwsza=liczby[j]
    zmienna=liczby[j]
    for i in range(j+1,N):
        n=nwd(zmienna,liczby[i])
        if n>1:
            zmienna=n
            dl+=1
        if n==1 or i==N-1:
            if dlmax<dl:
                dlmax=dl
                pierwszamax=pierwsza
                dzielmax=zmienna
            break
print(pierwszamax,dlmax,dzielmax)







