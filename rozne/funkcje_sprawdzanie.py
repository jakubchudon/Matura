import math
tablica=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
wynik=0
plik=open('/Users/jakubchudon/Desktop/matura2019/Dane_PR/liczby.txt')
for linia in plik:
   linia1=int(linia.strip())
   x=math.log(linia1,3)
   print(linia1,int(x),x)
   if x == int(x):
       wynik+=1
# print(wynik)
# t=[]
# i=0
# p=1
# while True:
#     p=3**i
#     t.append(p)
#     if p>100000:
#         break
#     i+=1
# zlicz=0
# plik=open('/Users/jakubchudon/Desktop/matura2019/Dane_PR/liczby.txt')
# x=plik.readlines()
# plik.close()
# for a in x:
#     a=int(a.strip())
#     if a in t:
#         zlicz+=1
# print(zlicz)
# import funkcje
# n=funkcje.nwd(int(4),int(2))
# print(n)
