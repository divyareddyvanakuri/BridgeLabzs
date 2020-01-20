from utilityofnode import Node
class satcklinkedlist:  
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
        temp_node = self.head
        while temp_node!=None:
            print(temp_node.data,end=",")
            temp_node = temp_node.next
        print("NULL")
    def pop(self):
        current_node = self.head
        self.head = current_node.next
        current_node = None
    def isEmpty(self):
        return self.head==None
    def reverse(self):
        previous = None
        current_node = self.head
        while current_node.next!=None:
            next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next
        self.head = previous
    def size(self):
        current = self.head
        count = 0
        while current.next!=None:
            current = current.next
            count += 1     
        return count 