try:
    lower = int(input("Enter lower range value:"))
    upper = int(input("Enter upper range value:"))
    import sys
    sys.path.append("/home/user/Desktop/programming/Datastructure")
    from DatastructureUtility import utilityofstackusinglinkedlist

    def primeanagrams(lower,upper):
        prime_list=[]
        for val in range(lower,upper+1):
            if val>1:
                for n in range(2,val):
                    if (val%n) == 0:
                        break
                else:
                    prime_list.append(val)
        anagram_list=[]
        for i in prime_list:
            for j in prime_list:
                if i != j and sorted(str(i))==sorted(str(j)):
                    anagram_list.append(i) 
        return set(anagram_list)
    mylist=list(primeanagrams(lower,upper))
    mylist.sort()


    mylinkedlist = utilityofstackusinglinkedlist.satcklinkedlist()
    for item in mylist:
        mylinkedlist.add_node(item)
    print("size of linked list:",mylinkedlist.size())
    mylinkedlist.pop()
    mylinkedlist.reverse()
    mylinkedlist.traverse()
    print("Linked list is Empty:",mylinkedlist.isEmpty())
except ValueError:
    print("Oops!  That was no valid number.  Try again...")