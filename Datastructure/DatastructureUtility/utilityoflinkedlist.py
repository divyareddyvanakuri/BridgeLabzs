from utilityofnode import Node
class utility:
    def __init__(self):
        self.head=None
        self.count=0
   
    def add_node(self,data):
        new_node= Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def remove(self,item):
        temp_node = self.head
        if temp_node and temp_node.data==item:
            self.head = temp_node.next
            temp_node = None
            return
        previous = None
        while temp_node and temp_node.data!=item:
            previous = temp_node
            temp_node = temp_node.next
        previous.next = temp_node.next


    def traverse(self):
        temp_node = self.head
        while temp_node!=None:
            print(temp_node.data,end=",")
            temp_node = temp_node.next
        print("NULL")

    def search(self,item):
        temp_node = self.head
        Found = False
        while temp_node!=None and not Found:
            if temp_node.data == item:
                Found = True
            else:
                temp_node = temp_node.next
        return Found
    
    def isEmpty(self):
        return self.head==None
    
    def Nodecount(self):
        temp_node = self.head
        while temp_node.next!=None:
            self.count += 1
            temp_node = temp_node.next
        return self.count
    
    def append(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp_node=self.head
            while temp_node.next!=None:
                temp_node=temp_node.next
            self.head = temp_node.next
            temp_node.next = new_node
    
    def Index(self,item):
        temp_node = self.head
        count = 0
        while temp_node!=None:
            if temp_node.data==item:
                return count
            temp_node = temp_node.next
            count += 1
        else:
            print("item not found in list")
    
    def insertion(self,data,position):
            count=0
            temp_node=self.head
            if(position==0):
                newnode=Node(data)
                newnode.next=temp_node
                temp_node=newnode
            elif(position>self.count):
                print("\n\nIndex is out of range\n\n")
            elif(position==self.count):
                self.append(data)
            else:
                previous = None
                while temp_node.next!=None and count!=position:
                    previous = temp_node
                    temp_node = temp_node.next
                    count += 1
                newnode=Node(data)
                previous.next = newnode
                newnode.next=temp_node.next
    
    def pop(self):
        this_node=self.head
        previous = None
        while this_node.next!=None:
            previous = this_node
            this_node = this_node.next
        previous.next = None    
    
    def popTheposition(self,pos):
        temp_node = self.head
        previous = None
        while temp_node.next!=None and pos>0:
            previous = temp_node
            temp_node = temp_node.next
            pos -= 1
        if previous==None:
            self.head = temp_node.next
        else:
            previous.next = temp_node.next
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