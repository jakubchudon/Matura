import random
tablica=[]
pierwsze=[]
i = 0
l=100
while i <= l:
    tablica.append(random.randint(0,1000))
    i = i + 1
print(tablica)
for x in tablica:
    for dzielnik in range(2,x):
        if x% dzielnik ==0:
            break
    else:
        pierwsze.append(x)
print(pierwsze)
