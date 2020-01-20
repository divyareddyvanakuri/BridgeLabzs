mylist = []
lower = 0
upper = 1000
for number in range(lower,upper):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
           mylist.append(number)
print(len(mylist))
prime = [[0 for i in range(20)]for j in range(0)]
print(prime)