class utility:
    def __init__(self,queue=[]*6,cash=[0]*6):
        self.queue=queue
        self.cash=cash
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        del self.queue[0]
    def get_queue(self):
        return self.queue
    def isEmpty(self):
        return self.queue==[]
    def size(self):
        return len(self.queue)