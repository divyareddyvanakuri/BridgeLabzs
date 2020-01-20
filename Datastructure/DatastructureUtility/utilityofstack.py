class utility:
    def __init__(self,stack=[]):
        self.stack=stack
    def push(self,item):
        self.stack.append(item)
    def Pop(self):
        self.stack.pop()
    def is_empty(self):
        return self.stack ==[]
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def get_stack(self):
        return self.stack
    def size(self):
        return len(self.stack)