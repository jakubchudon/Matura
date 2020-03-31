plik=open('/Users/jakubchudon/Desktop/slowa.txt')
w=0
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    x=linia[0]
    y=linia[1]
    if x.endswith('A'):
        w+=1
    if y.endswith('A'):
        w+=1
print(w)