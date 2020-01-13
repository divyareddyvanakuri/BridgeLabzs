#node object class
my_list = []
with open("text","r") as f:
    my_list = f.read().split()
print(my_list)
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
    def add_node(self,data):
        self.count += 1
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
    def search(self,item):
        temp_node = self.head
        Found = False
        while temp_node!=None and not Found:
            if temp_node.data == item:
                Found = True
            else:
                temp_node = temp_node.next
        return Found
    def del_node(self,item):
        self.count -= 1
        temp_node = self.head
        previous = None
        Found = False
        while  not Found:
            if temp_node.data == item:
                Found = True
            else:
                previous = temp_node
                temp_node = temp_node.next
        if temp_node.next==None:
            self.head = temp_node.next
        else:
            previous.next = temp_node.next
    def count_Node(self):
        print(self.count)

mylist=linked_list()
for data in my_list:
    mylist.add_node(data)
mylist.traverse()
word = input("enter key word:")
if mylist.search(word)==False:
    mylist.add_node(word)
    with open("text","a") as f:
        my_list = f.write(" "+word)
else:
    mylist.del_node(word)
    for i in range(len(my_list)-1):
        if my_list[i] == word:
            del my_list[i] 
    with open('text', 'w') as f:
        for listitem in my_list:
            f.write('%s\n' % listitem)
mylist.count_Node()
print(my_list)