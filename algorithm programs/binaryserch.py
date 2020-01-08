'''f = open("text","r") 
my_list=[]
for x in f:
    my_list.extend(x.split())
print(my_list)
f.closed'''
my_list=[]
with open("text","r") as f:
    my_list = f.read().split()
def binaryserach(my_list,low,high,word):
    mid = low+(high-low)//2
    Found = False
    while low<=high and not Found:
        if word==my_list[mid]:
            return mid
            Found = True
        elif word<my_list[mid]:
            return binaryserach(my_list,low,mid-1,word)
        else:
            return binaryserach(my_list,mid+1,high,word)
my_list.sort()
print(my_list)
word = input("enter name:")
result = binaryserach(my_list,0,len(my_list)-1,word)
print("key word is founded in position of:",result)



