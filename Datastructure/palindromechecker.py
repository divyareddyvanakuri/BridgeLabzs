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
    def palindrome_checker(self):
        return self.deque[0:]==self.deque[::-1]

mydeque = Deque()
print(mydeque.isEmpty())
string = input("enter a string:")
for i in range(len(string)-1,-1,-1):
    mydeque.addFront(string[i])
print(mydeque.get_deque())
print(mydeque.palindrome_checker())
mydeque.addRear(2,'g')
print(mydeque.get_deque())
mydeque.removeFront()
print(mydeque.get_deque())
mydeque.removeRear('g')
print(mydeque.get_deque())
print(mydeque.Size())
