class utility:
    def __init__(self):
        self.sizeofhashtable=11
        self.hashtable = [[] for _ in range(self.sizeofhashtable)]
    def hashfunction(self,element):
        return element%self.sizeofhashtable
    def get_hashtable(self):
        return self.hashtable
    def insertion(self, Value):
        hash_key = self.hashfunction(Value)
        if self.hashtable[hash_key] == None:
            self.hashtable[hash_key] = Value
        else:
            if type(self.hashtable[hash_key]) == list:
                self.hashtable[hash_key].append(Value)
            else:
                self.hashtable[hash_key] = [self.hashtable[hash_key], Value]
        
    def search(self,Value):
        hash_key=self.hashfunction(Value)
        for i in range(len(self.hashtable[hash_key])):
            if self.hashtable[hash_key][i]==Value:
                return True
            else:
                return False
    def remove(self,Value):
        hash_key=self.hashfunction(Value)
        self.length = len(self.hashtable[hash_key])
        if self.length==1:
            self.hashtable[hash_key]=[]
        else:
            for i in range(self.length-1):
                if self.hashtable[hash_key][i]==Value:
                    del self.hashtable[hash_key][i]