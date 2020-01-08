import random
goal = int(input("enter your goal stack:"))
stack = int(input("enter number of stacks you have:"))
win = 0
count =0 
while stack>0:
        count += 1
        die = random.randint(1,4)
        print()
        choice1 = int(input("enter first guess"))
        print()
        choice2 = int(input("enter second guess"))
        print ('die rolling done..')
        if choice1==die or choice2 ==die:
                stack += 1
                print ('rolled one',die)
                print ('win! you won $1, you\'re new balance is:',stack)
                win += 1
        else:
            stack -= 1
            print ('rolled one',die)
            print ('lose! you lost $1, you\'re new balance is:',stack)
        if stack<0:
            print ('Bankrupt.')
            quit()
        if stack==goal:
            print ('Millionaire!')
            break    
print("number of wins",win)
perwin = win/count*100
perloss = 100 - perwin
print("percentag of win:",perwin)
print("percentage of loss:",perloss)
