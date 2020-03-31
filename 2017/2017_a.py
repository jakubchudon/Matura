plik=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/dane.txt")
odp=open("C:/Users/Jakub/PycharmProjects/Matura/Pliki/2017_maj/odp_6.1.txt",'w')
jasny=0
ciemny=265
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    for x in linia:
        if int(x)>jasny:
            jasny=int(x)
        if int(x)<ciemny:
            ciemny=int(x)
print(jasny,ciemny)
odp.write(str(jasny)+" "+str(ciemny))
