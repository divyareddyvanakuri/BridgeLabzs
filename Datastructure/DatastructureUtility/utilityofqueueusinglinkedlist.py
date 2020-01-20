from utilityofnode import Node
class queuelinkedlist:  
    def __init__(self,head=None):
        self.head=head
        self.count=0
    def add_node(self,data):
        new_node= Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def traverse(self):
        current = self.head
        while current.next!=None:
            print(current.data,end=",")
            current = current.next
        print("Null")
    def pop(self):
        this_node=self.head
        previous = None
        while this_node.next!=None:
            previous = this_node
            this_node = this_node.next
        previous.next = None    
    def isEmpty(self):
        return self.head == None
    def size(self):
        current = self.head
        count = 0
        while current.next!=None:
            current = current.next
            count += 1
        return count