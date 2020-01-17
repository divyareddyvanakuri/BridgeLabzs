mylist = []
with open("listofnumbers",'r') as f:
    mylist = f.read().split(",")
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
    def sort(self):
        current = self.head
        index = None
        if self.head == None:
            return 
        else:
            while current != None:
                index = current.next
                while index != None:
                    if index.data<current.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    else:
                        index = index.next
                current = current.next
Mylist = orderedlinkedlist()
for data in mylist:
    Mylist.add_node(data)
#Mylist.traverse()
Mylist.add_node('57')
Mylist.sort()
Mylist.traverse()