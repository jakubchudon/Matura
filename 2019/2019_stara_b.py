plik=open('C:/Users/Jakub/PycharmProjects/Matura/Pliki/2019_stara_maj/dzialki.txt')
normalne=[]
nor=''
odwrocone=[]
for linia in plik:
    linia=linia.strip()
    if linia!="":
        nor+=linia
    else:
        normalne.append(nor)
        odwrocone.append(nor[::-1])
        nor=''
wyniki=[]
nr1=1
for x in normalne:
    nr2=1
    for y in odwrocone:
        if x==y:
            o=str(nr1)+" "+str(nr2)
            wyniki.append(o)
        nr2+=1
    nr1+=1
for i in range(len(wyniki)-1):
    if wyniki[i]!=wyniki[i+1]:
        print(wyniki[i])


