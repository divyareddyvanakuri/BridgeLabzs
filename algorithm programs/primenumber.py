lower = 0
upper = 1000
for val in range(lower,upper+1):
    if val>1:
        for n in range(2,val):
            if (val%n) == 0:
                break
        else:
            print(val)