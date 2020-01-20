
import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityofCollisionResolutionwithchaining
Myhashtable = utilityofCollisionResolutionwithchaining.utility()
mylist = [77,26,82,13,14,12,15,86,97,67]
for item in mylist:
    Myhashtable.insertion(item)
number = int(input("enter number:"))
if Myhashtable.search(number)==False:
    Myhashtable.insertion(number)
    mylist.append(number)
else:
    Myhashtable.remove(number)
    mylist.remove(number)
print(Myhashtable.get_hashtable())