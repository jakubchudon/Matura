slowa=open('/Users/jakubchudon/Desktop/matury/2015_podstawa/slowa.txt')
nowe=open('/Users/jakubchudon/Desktop/matury/2015_podstawa/nowe.txt')
tab_s=[]
for linia in slowa:
    tab_s.append(linia.strip())
for linia in nowe:
    linia=linia.strip()
    x=tab_s.count(linia)
    y=tab_s.count(linia[::-1])
    print(linia,x,y)