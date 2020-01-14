class Queue():
    def __init__(self,queue=[],length_queue=7):
        self.queue=queue
        self.length_queue=length_queue
    def push(self,val):
        self.queue.append(val)
    def pop(self):
        del self.queue[0]
    def get_queue(self):
        return self.queue

myqueue = Queue()
myqueue.push(7)
myqueue.push(8)
myqueue.push(9)
myqueue.push(10)
myqueue.push(11)
print(myqueue.get_queue())
myqueue.pop()
print(myqueue.get_queue())