import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityoflinkedlist
try:
    mylist = []
    with open("listofnumbers",'r') as f:
        mylist = f.read().split()

except FileNotFoundError:
    print("Oops!  No such file or directory.  Try again...")

else:
    Mylinkedlist = utilityoflinkedlist.utility()
    print(Mylinkedlist.isEmpty())
    for data in mylist:
        Mylinkedlist.add_node(data)

    number = input("enter a number:")
    if Mylinkedlist.search(number)==True:
        Mylinkedlist.remove(number)
        for i in range(len(mylist)-1):
            if str(number)==mylist[i]:
                del mylist[i]
    else:
        Mylinkedlist.add_node(number)
        mylist.append(number)
    Mylinkedlist.sort()
    Mylinkedlist.traverse()
    print(mylist)
    with open("listofnumbers",'w') as f:
        for item in mylist:
            f.write(item+"\n")
finally:
    print("executing finally clause")
