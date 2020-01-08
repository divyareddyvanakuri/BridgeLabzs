my_list = [56,2,-67,47,38,0,33]
for j in range(len(my_list)-1,0,-1):
    for i in range(j):
        if my_list[i]>my_list[i+1]:
            my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
print(my_list)