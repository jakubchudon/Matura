initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
while year <= maxTimeYears:
    initialCapital = round(initialCapital + (initialCapital*percent))
    print(year,initialCapital)
    year=year+1