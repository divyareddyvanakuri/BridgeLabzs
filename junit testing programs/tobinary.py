x =format(100,'08b')
lst = list(x)
n = len(lst)//2
lst1 = lst[n:]
lst2 = lst[:n]
new_list = lst1+lst2
c = " "
for i in new_list:
    c += i
num = int(c,2)
print(num)
    