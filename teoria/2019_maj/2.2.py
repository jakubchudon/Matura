def pisz(s,n,k):
    if len(s)==n:
        print(s)
    else:
        for i in range(0,k):
            pisz(s+str(i),n,k)
pisz("",2,3)
print(2+3)