slowo='xxxxx yyyyy ccccc'
dl=len(slowo)
i=0
tekst=''
while slowo[i]!=" ":
    tekst+=slowo[i]
    if i==dl:
        break
    if slowo[i+1]==' ':
        print(tekst)
        tekst=''
        i=i+1
    i=i+1


