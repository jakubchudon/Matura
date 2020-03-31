plik=(open('/Users/jakubchudon/Desktop/matury/2014_podstawa/Pary_liczb.txt'))
wynik=0
def nwd(a,b):
    while int(a)%int(b) !=0:
        r=a%b
        a=b
        b=r
    return b
for linia in plik:
    linia=linia.split()
    x=int(linia[0])
    y=int(linia[1])
    if nwd(x,y)==1:
            wynik+=1
print(wynik)