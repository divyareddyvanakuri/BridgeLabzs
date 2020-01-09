def insersort(my_list):
    for index in range(1,len(my_list)):
        current_element=my_list[index] #c
        pos = index #1
        j =0
        Found = False
        while pos>0 and not Found:
            if j<3:
                mini = current_element[j] #c
                maxi = my_list[pos-1][j] #s
                if mini == maxi:
                    j += 1
                elif ord(mini)<ord(maxi): #c < #s 
                    my_list[pos] = my_list[pos-1]
                    pos -= 1
                else:
                    Found = True                
        my_list[pos] = current_element
my_list = ["kai","bambam","suho","sehun","chen","chanyeol"]
insersort(my_list)
print(my_list)