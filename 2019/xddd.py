def rek(x,p,k):
    T=[1,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17]
    if p<k:
        s=(p+k)//2
        if T[s]>=x:
            return rek(x,p,s)
        else:
            rek(x,s+1,k)
    else:
        if T[p]==x:
            return p
        else:
            return (-1)
hh=rek(2020,5,14)
print(hh)