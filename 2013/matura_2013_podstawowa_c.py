plik=open('/Users/jakubchudon/Desktop/matury/2013_podstawa/napisy.txt')
same_zera=0
same_jeynki=0
for linia in plik:
    linia=str(linia.strip())
    dl=len(linia)
    if linia.count("0")==dl:
        same_zera+=1
    if linia.count("1")==dl:
        same_jeynki+=1
print("same zera",same_zera)
print("same jedynki",same_jeynki)

