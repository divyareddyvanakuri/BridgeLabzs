import random
numberofcoupons=int(input("enter number of coupons:"))
couponrange = int(input("enter coupon range"))
print("coupons:")
chars = 'abcdefghijklmnopqrstvuwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$!'
for j in range(numberofcoupons):
    for i in range(couponrange):
        x  ="".join(random.sample(chars,k=1))
        print(x,end="")
    print()