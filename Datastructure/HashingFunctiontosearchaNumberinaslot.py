class hashTable:
    def __init__(self):
        self.sizeofhashtable=10
        self.hashtable = [None]*self.sizeofhashtable
    def hashfuction(self,value,key=0):
        self.value = value
        self.key = self.value%self.sizeofhashtable
        self.hashtable[self.key]=self.value
    def get_hashtable(self):
        return self.hashtable
Myhashtable = hashTable()
mylist = [45,67,78,60,89]
for i in mylist:
    Myhashtable.hashfuction(i)
print(Myhashtable.get_hashtable())