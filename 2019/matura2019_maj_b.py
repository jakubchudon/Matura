from funkcje import suma_silnia
plik=open('/Users/jakubchudon/Desktop/matura2019/Dane_PR/liczby.txt')
for linia in plik:
    linia1=int(linia.strip())
    w=linia1
    x=suma_silnia(w)
    if x==w:
        print(linia1)


