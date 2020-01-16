class Queue():
    def __init__(self,queue=[]*6,cash=[0]*6):
        self.queue=queue
        self.cash=cash
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        del self.queue[0]
    def get_queue(self):
        return self.queue
    def isEmpty(self):
        return self.queue==[]
    def size(self):
        return len(self.queue)
    def cash_withdraw(self,amount,pos):
        self.amount=amount
        self.pos=pos
        if 100<amount<self.cash[pos]:
            self.cash[self.pos] -= self.amount
            print("Balance Amount")
            print(self.queue[self.pos],":",self.cash[pos])
        else:
            print("Ensure about amount of Money in your Account")
            print(self.queue[pos],":",self.cash[pos])
    def cash_Deposit(self,amount,pos):
        self.amount=amount
        self.pos=pos
        self.cash[self.pos] += self.amount
        print("Balance Amount")
        print(self.queue[self.pos],":",self.cash[pos])
        

myqueue = Queue()
print(myqueue.isEmpty())
Names = ["kai","suho"]
for i in range(len(Names)):
    myqueue.enqueue(Names[i])
print(myqueue.size())
print(myqueue.get_queue())
customer_name = input("enter name:")
if customer_name in myqueue.get_queue():
    pos = Names.index(customer_name)
    print("Cash Counter Menu:")
    print(" 1.cash withdraw")
    print(" 2.cash deposit")
    option = int(input("select option:"))
    if option == 1:
        amount =  float(input("enter amount of money to withdraw:"))
        myqueue.cash_withdraw(amount,pos)
    elif option == 2:
        amount =  float(input("enter amount of money to deposit:"))
        myqueue.cash_Deposit(amount,pos)
else:
    print("ensure about user name")