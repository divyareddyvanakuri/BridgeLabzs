class Deque:
    def __init__(self,deque=[]):
        self.deque=deque
    def addFront(self,item):
        self.deque.append(item)
    def addRear(self,pos,item):
        self.deque.insert(pos,item)
    def removeFront(self):
        del self.deque[0]
    def removeRear(self,item):
        self.deque.remove(item)
    def isEmpty(self):
        return self.deque==[]
    def Size(self):
        return len(self.deque)
    def get_deque(self):
        return self.deque
string = "Divya"
mydeque = Deque()
for i in range(len(string)-1,-1,-1):
    mydeque.addFront(string[i])
print(mydeque.get_deque())
mydeque.addRear(2,'g')
print(mydeque.get_deque())
mydeque.removeFront()
print(mydeque.get_deque())
print(mydeque.isEmpty())
print(mydeque.Size())