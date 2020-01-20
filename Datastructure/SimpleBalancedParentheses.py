import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityofstack

mystack = utilityofstack.utility()
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