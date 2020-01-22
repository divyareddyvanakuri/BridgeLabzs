import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityofDeque

mydeque = utilityofDeque.utility()
print("IsEmpty Deque:",mydeque.isEmpty())
string = input("enter a string:")
for i in range(len(string)):
    mydeque.addFront(string[i])

print("Given string size:",mydeque.Size())
mydeque.addRear(0,'g')
mydeque.removeRear('g')
print(mydeque.get_deque())
if mydeque.palindrome_checker() is True:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")
