for x in range(2,31):
    for dzielnik in range(2,x):
        if x% dzielnik ==0:
            break
    else:
            print(x,"jest pierwsza")