# x='M'
# y=ord(x)
# w=chr(y)
# print(w)
# tekst_zaszyfrowany=""
# wyraz="MARTA"
# kod="TOR"
# while len(wyraz) > len(kod):
#     kod = kod + kod
# for p in range(len(wyraz)):
#     zmienna=0
#     w=wyraz[p]
#     r=kod[p]
#     t=ord(wyraz[p])
#     u=ord(kod[p])
#     x=ord(wyraz[p])+(ord(kod[p])-64)
#     while x>90:
#         x=x-26
#     tekst_zaszyfrowany+=chr(x)
# print(tekst_zaszyfrowany)
tab1=[] 
tab2=[]
test1=open("C:/matura/2014/test.txt")
test2=open("C:/matura/2014/test1.txt")
for line in test1:
    tab1.append(line.strip())
for line in test2:
    tab2.append(line.strip())
if tab1==tab2:
    print("GIT")
