def pierwiastek(x):
    x=int(x)
    dokladnosc=float(0.001)
    b=1
    b=float(b)
    while abs(b-((b+(x/b))/2)) > dokladnosc:
        b=((b+(x/b))/2)
    else:
        return round(b,2)
x=[1,2,3]
print(sum(x))