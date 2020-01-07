num = int(input("enter number: "))
lower = int(input("enter lower range: "))
upper = int(input("enter upper range: "))
lst = []
for i in range(lower,upper):
    if num%i==0:
        lst.append(i)
print("factors between", lower, "and", upper, "are:")
print(lst)
k=0
print("Prime factors between", lower, "and", upper, "are:")
for k in range(0,len(lst)): 
    for i in range(2, lst[k]):    
       if (lst[k] % i) == 0: 
           break
    else:
        print(lst[k])