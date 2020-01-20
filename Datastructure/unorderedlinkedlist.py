import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityoflinkedlist


mylist = []
with open("text","r") as f:
    mylist = f.read().split()
print(mylist)


myLinkedlList=utilityoflinkedlist.utility()
print(myLinkedlList.isEmpty())
for data in mylist:
    myLinkedlList.add_node(data)
word = input("serach word:")
if myLinkedlList.search(word)==True:
    myLinkedlList.remove(word)
    for i in range(len(mylist)-1):
        if word==mylist[i]:
            del mylist[i]
else:
    myLinkedlList.append(word)
    mylist.append(word)
myLinkedlList.traverse()
print(mylist)
with open("text",'w') as f:
    for item in mylist:
     f.write(item+"\n")

