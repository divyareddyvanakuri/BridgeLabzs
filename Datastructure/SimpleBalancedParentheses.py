class Stack:
    def __init__(self,stack=[]):
        self.stack=stack
    def is_empty(self):
        return self.stack ==[]
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def get_stack(self):
        return self.stack
    def size(self):
        return len(self.stack)
    def Check_for_balance(self,items):
        self.items=items
        n = len(self.items)
        for i in range(n):
            if self.items[i]=="(":
                self.stack.append(a[i])
            elif self.items[i]==")":
                if len(self.items)>0:
                    self.stack.pop()
        if len(self.stack)==0:
            return "balanced"
        else:
            return "Unbalanced"
mystack = Stack()
a = "(5+6)∗(7+8)/((4+3)(5+6)∗(7+8)/(4+3)"
items=[]
for i in range(len(a)):
    items.append(a[i])
print(mystack.Check_for_balance(items))
print(mystack.peek())
print(mystack.is_empty())
print(mystack.size())
                