plik=open('/Users/jakubchudon/Desktop/slowa.txt')
# # w=0
# # for linia in plik:
# #     linia=linia.strip()
# #     linia=linia.split()
# #     x=linia[0]
# #     y=linia[1]
# #     if len(x)<=len(y):
# #         w1=0
#         for i in range(len(x)):
#             for n in range(len(y)):
#                 if x[i]==y[n]:
#                     w1+=1
#                     break
#         else:
#             if w1==len(x):
#                 w+=1
# print(w)
w=0
for linia in plik:
    linia=linia.strip()
    linia=linia.split()
    x=linia[0]
    y=linia[1]
    if x==y:
        w+=1
    if len(x)<len(y):
        a=len(y)-len(x)+1
        for i in  range(a):
            if y[i:i+len(x)]==x :
                w+=1
                break
print(w)