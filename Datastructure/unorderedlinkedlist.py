
#node object class
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next=next
class linked_list:
    def __init__(self):
        self.head=None
        self.count=0
    def isEmpty(self):
        return self.head==None
    def add_front_node(self,data):
        self.count += 1
        new_node= Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def add_end_node(self,data):
        self.count += 1
        new_node = Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp_node = self.head
            while temp_node.next!=None:
                temp_node = temp_node.next
            temp_node.next = new_node
    def traverse(self):
        temp_node = self.head
        while temp_node!=None:
            print(temp_node.data)
            temp_node = temp_node.next
        print("NULL")
  
mylist=linked_list()
mylist.add_front_node(4)
mylist.add_front_node(99)
mylist.add_front_node(98)
mylist.add_end_node(18)
mylist.add_end_node(8)
mylist.traverse()



    