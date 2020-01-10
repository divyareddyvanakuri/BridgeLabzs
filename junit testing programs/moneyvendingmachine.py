print("welcome to drinks machine")
print("menu:")
print(" 1.waterbottle-20/-")
print(" 2.cola-30/-")
print(" 3.tea-10/-")
water = 20
cola = 30
tea = 10
money = int(input("enter Amount of money:"))
choice = int(input("enter your choice of drink: "))
if choice==1:
    print("your selected waterbottle..")
    money -= water
    print("balance :",money)
elif choice==2:
    print("your selected cola..")
    money -= cola
    print("balance :",money)
elif choice==3:
    print("your selected cola..")
    money -= tea
    print("balance :",tea)
else:
    print("ensure about your choice please enter between 1 t0 3")
