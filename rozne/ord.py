wyraz='edamo'
dlugosc=len(wyraz)
for znak in range(0,dlugosc):
    a=znak
    b=znak+1
    if ord(wyraz[a])+ ord(wyraz[b])== 220:
        break
    else:
        print(wyraz)