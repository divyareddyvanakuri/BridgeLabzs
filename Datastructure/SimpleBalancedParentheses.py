class Stack:
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
mystack = Stack()
a = input("Take Any Arithmetic Expression or Parentheses Expression:")
print("Input:",a)
open_list = ["(","[","{"]
closed_list = [")","]","}"]
for i in range(len(a)):
    if a[i] in open_list:
        mystack.push(a[i])
    elif a[i] in closed_list:
        if mystack.size()>0:
            mystack.Pop()
if mystack.is_empty():
    print("balanced")
else:
    print("unbalanced")
    print(mystack.peek())
print(mystack.get_stack())
                