# investment - compound interest rate
inv = int(input('give me ur money'))
perc = float(input('percent'))
percent = perc/100
interest = inv*percent
ninv = inv
years = 0
while ninv < inv*2:
    ninv = ninv + ninv * percent
    print(ninv)
    years+=1
    print(years,"year/s")

