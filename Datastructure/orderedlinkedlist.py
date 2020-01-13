mylist = []
with open("text1",'r') as f:
    mylist = f.read().split()
mylist.sort(reverse=True)
print(mylist)
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class orderedlinkedlist:
    def __init__(self,head=None):
        self.head=head
    def add_node(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node
    def traverse(self):
        temp_node = self.head
        while temp_node!=None:
            print(temp_node.data)
            temp_node = temp_node.next
        print("Null")
Mylist = orderedlinkedlist()
for data in mylist:
    Mylist.add_node(data)
Mylist.traverse()