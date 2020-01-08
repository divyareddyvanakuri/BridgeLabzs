def insersort(my_list):
    for index in range(1,len(my_list)):
        current_element=my_list[index] #c
        pos = index #1
        while current_element<my_list[pos-1] and pos>0:
            mini = current_element[0] #c
            maxi = my_list[pos-1][0] #s
            if ord(mini)<ord(maxi): #c < #s 
                my_list[pos] = my_list[pos-1]
            pos -= 1
        my_list[pos] = current_element
my_list=["suho","chanyeol","beaykhun","kai","jinyoung","mark","xiumin"]
#my_list=[45,-7,34,0,3,56,3]
insersort(my_list)
print(my_list)
    
    
    


