import random
tablica=[]
pierwsze=[]
i = 0
l=5
for i in range(l):
    tablica.append(random.randint(0,1000))
print(tablica)
index=0
list=[]
for x in tablica:
    for dzielnik in range(2,x):
        if x% dzielnik ==0:
            index=index+1
            break
    else:
        index=index+1
        list.append(index)
        pierwsze.append(x)
print(pierwsze)
print(list)
i=0
suma_cyfr=[]
for number in pierwsze:
    tmpnumber = number
    sumOfDigits = 0
    while tmpnumber >0:
        digit = tmpnumber % 10
        sumOfDigits += digit
        tmpnumber = tmpnumber//10
    else:
        suma_cyfr.append(sumOfDigits)
print(suma_cyfr)
super_pierwsze=[]
for y in suma_cyfr:
    for dzielnik in range(2,y):
        if y% dzielnik ==0:
            break
    else:
        super_pierwsze.append(y)
print(super_pierwsze)








