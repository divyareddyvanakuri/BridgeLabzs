print("welcome to money  vending machine")
a = [1,2,5,10,50,100,500,1000]
atm = [0,0,0,0,0,0,0]
money = int(input("enter amount:"))
for i in a[::-1]:
    flog = 0
    for j in atm:
        if money//i!=0:
            j += 1
            print(i,":",j)s
            money -= i
            flog = 1
            