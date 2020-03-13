from funkcje import suuma_cyfr
plik=open('/Users/jakubchudon/Desktop/matury/2012_podstawa/cyfry.txt')
min=90
maks=0
for linia in plik:
    linia=int(linia.strip())
    x=suuma_cyfr(linia)
    if x>suuma_cyfr(maks):
        maks=linia
    if x<suuma_cyfr(min):
        min=linia
print(min,maks)
