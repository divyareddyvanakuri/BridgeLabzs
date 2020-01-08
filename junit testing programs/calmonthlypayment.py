p = float(input("enter principal loan amount:"))
y = int(input("enter make over years:"))
R = float(input("enter monthly rate of interest:"))
n = 12 * y
r = R /(12*100)
payment = round(p*r/(1-(1+r)**(-n)),3)
print(payment)