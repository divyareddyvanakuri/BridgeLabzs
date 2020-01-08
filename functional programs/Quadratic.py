import cmath
def qadraticeq(a,b,c):
    d = (b*b) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print("root1:",sol1)
    print("root2:",sol2)
a ,b ,c = [int(a) for a in input("enter constant values a,b,c:").split()]
qadraticeq(a,b,c)