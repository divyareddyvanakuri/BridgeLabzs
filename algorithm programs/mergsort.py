def mergesort(my_list):
    if len(my_list)>1:
        mid = len(my_list)//2
        left_list=my_list[:mid]
        right_list=my_list[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                my_list[k] = left_list[i]
                i += 1
                k += 1
            else:
                my_list[k]=right_list[j]
                j += 1
                k += 1
        while i<len(left_list):
            my_list[k] = left_list[i]
            i += 1
            k += 1
        while j<len(right_list):
            my_list[k]=right_list[j]
            j += 1
            k += 1
my_list = ["kai","chan","suho","aOi","got7","bambam","mark","jinyoung"]
mergesort(my_list)
print("sorted list is:",my_list)