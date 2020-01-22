import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityofqueue
myqueue = utilityofqueue.utility()
def is_expression_balanced(p_expression):
    if type(p_expression) is int:
        return False

    open_list=['(','{','[']
    closed_list = [')','}',']']
    for index in range(len(p_expression)):
        if p_expression[index] in closed_list:
            myqueue.enqueue(p_expression[index])
    mylist = myqueue.get_queue()
    
    for index in range(len(p_expression)-1,-1,-1):
        if  p_expression[index] in open_list:
            pos = open_list.index(p_expression[index])
            if myqueue.size()>0 and closed_list[pos] == mylist[len(mylist)-1]:
                myqueue.dequeue()
            else:
                myqueue.enqueue(p_expression[index])
    
    if myqueue.size() == 0:
        return True
    else:
        return False
     

