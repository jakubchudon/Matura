plik=open('/Users/jakubchudon/Desktop/dane.txt')
for linia in plik:
    x=len(linia)
    if (int(x))%2==0:
        for i in range(0,x-1):
            if linia[i]>linia[i+1]:
                break
        else:
            print(linia)
