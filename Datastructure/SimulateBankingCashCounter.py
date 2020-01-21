import sys
sys.path.append("/home/user/Desktop/programming/Datastructure")
from DatastructureUtility import utilityofqueue
def cash_withdraw(self,amount,pos=0):
    self.amount=amount
    self.pos=pos
    if 100<amount<self.cash[pos]:
        self.cash[self.pos] -= self.amount
        print("Balance Amount")
        print(self.queue[self.pos],":",self.cash[pos])
    else:
        print("Ensure about amount of Money in your Account")
        print(self.queue[pos],":",self.cash[pos])
def cash_Deposit(self,amount,pos=0):
    self.amount=amount
    self.pos=pos
    self.cash[self.pos] += self.amount
    print("Balance Amount")
    print(self.queue[self.pos],":",self.cash[pos])
def createAmount():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to create a New amount in our Bank? (yes or no)')
    return input().lower().startswith('y')
myqueue = utilityofqueue.utility()
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
    print(" 3.Delet amount")
    option = int(input("select option:"))
    if option == 1:
        amount =  int(input("enter amount of money to withdraw:"))
        cash_withdraw(amount,pos)
    elif option == 2:
        amount =  int(input("enter amount of money to deposit:"))
        cash_Deposit(amount,pos)
    else:
        Names.remove(customer_name)
else:
    print("ensure about user name")
    if createAmount()==True:
        Names.append(customer_name)
        amount =  int(input("enter amount of money to deposit:"))
        cash_Deposit(amount,pos)
myqueue.dequeue()