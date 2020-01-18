mylist = []
with open("listofnumbers",'r') as f:
    mylist = f.read().split()
from utilityoforderedlinkedlist import utility
from Node import Node
Mylinkedlist = utility()
print(Mylinkedlist.isEmpty())
for data in mylist:
    Mylinkedlist.add_node(data)

number = input("enter number:")
if Mylinkedlist.serach(number)==True:
    Mylinkedlist.remove(number)
    for i in range(len(mylist)-1):
        if str(number)==mylist[i]:
            del mylist[i]
else:
    Mylinkedlist.add_node(number)
    mylist.append(number)
Mylinkedlist.sort()
Mylinkedlist.traverse()``
print(mylist)
with open("listofnumbers",'w') as f:
    for item in mylist:
     f.write(item+"\n")