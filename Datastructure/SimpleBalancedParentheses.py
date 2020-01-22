import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityofstack

mystack = utilityofstack.utility()
p_expression = input("Take Any Arithmetic Expression or Parentheses Expression:")

open_list = ["(","[","{"]
closed_list = [")","]","}"]


for i in range(len(p_expression)):
    if p_expression[i] in open_list:
        mystack.push(p_expression[i])
    elif p_expression[i] in closed_list:
        pos = closed_list.index(p_expression[i])
        mylist = mystack.get_stack()
        if mystack.size()>0 and open_list[pos] == mylist[len(mylist)-1]:
            mystack.Pop()
        else:
            mystack.push(p_expression[i])
if mystack.is_empty():
    print("balanced")
else:
    print("unbalanced")
    print(mystack.peek())
    print(mystack.get_stack())