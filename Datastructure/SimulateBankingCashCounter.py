class Queue():
    def __init__(self,queue=[],length_queue=7):
        self.queue=queue
        self.length_queue=length_queue
    def push(self,val):
        self.queue.append(val)
    def pop(self):
        del self.queue[0]
    def get_queue(self):
        return self.queue
    def isEmpty(self):
        return self.queue==[]
    def size(self):
        return len(self.queue)
myqueue = Queue()
Names = ["kai","suho","minho"]
cash = [1000,2000,3000]
for i,j in zip(Names,cash):
    print(i,":",j)
print("Cash Counter Menu:")
print(" 1.Cash withdraw")
print(" 2.Cash Deposit")

customer_name=input("enter User Name:")
if customer_name in Names:
    pos = Names.index(customer_name)
    Choice = int(input("select between 1 or 2:"))
    if Choice == 1:
        if customer_name in Names:
            amount = float(input("Enter withdraw amount:"))
            if 100<amount<cash[pos]:
                cash[pos] -= amount
                amount = cash[pos]
                cash.insert(pos,amount)
                print("Balance Amount")
                print(Names[pos],":",cash[pos])
            else:
                print("Ensure about amount of Money in your Account")
                print(Names[pos],":",cash[pos])
        else:
            print("Ensure user name needs to be valide one")
    elif Choice == 2:
        if customer_name in Names:
            amount = float(input("Enter Deposit amount:"))  
            cash[pos] += amount
            print("Balance Amount")
            print(Names[pos],":",cash[pos])
        else:
            print("Ensure user name needs to be valide one")
    else:
        print("please select valide choice")
else:
    print("User Name was Invalide")
    print()
    new_account_acceptance = input("you want to creat New Account in our Bank y or n:")
    if new_account_acceptance.lower()=='y':
        Names.append(customer_name)
        amount = float(input("Enter Amount of Money you want Deposit in your New Account:"))
        cash.append(amount)
    else:
        print("Have A Day")

