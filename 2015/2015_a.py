plik=open('/Users/jakubchudon/Desktop/matury/2015_podstawa/slowa.txt')
tab=[]
for linia in plik:
    tab.append(len(linia.strip()))
for i in range(1,13):
    print(i,tab.count(i))