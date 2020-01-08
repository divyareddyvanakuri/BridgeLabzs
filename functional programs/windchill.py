import math
def windchill(t,v):      
    return 35.74+0.6215*t+(0.4275*t-35.75)*math.pow(v,0.16)
print("calculation of windchill")
temp = input("enter temperature in  C or F:")
speed = input("enter speed in mph:")
t = 0
c1 = temp[-1]
d1=speed[-3:]
if d1.upper()=="MPH" and c1.upper()=="C" or c1.upper()=="F":
    c = int(temp[:-1])
    d = int(speed[:-3])
    if (c<50 and 3<d<120):
        if c1.upper()=='C':
            f = (9*c+32*5)/5
            t = f
        else:
            t = c
        v = d
        w = windchill(t,v)
        print("effective temperature (the wind chill) to be:",w)   
    else:
        print("enter temperature below 50c or 50f and speed between 3mph to 120mph")
else:
    print("enter valide units e.g., 45F or 10C and 23mph etc.")
