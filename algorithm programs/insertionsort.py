def insersort(my_list):
    for index in range(1,len(my_list)):
        current_element=my_list[index]
        pos = index 
        j =0
        Found = False
        while pos>0 and not Found:
            if j<3:
                mini = current_element[j] 
                maxi = my_list[pos-1][j] 
                if mini == maxi:
                    j += 1
                elif ord(mini)<ord(maxi):
                    my_list[pos] = my_list[pos-1]
                    pos -= 1
                else:
                    Found = True                
        my_list[pos] = current_element
my_list = ["kai","bambam","suho","sehun","beakhyun","chanyeol","chen","heechal","minho"]
insersort(my_list)
print(my_list)