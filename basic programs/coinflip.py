import random
def fun(tries):
    hcount = 0
    tcount = 0
    phead = 0
    ptail = 0
    flips = 0
    while flips<tries:
        flips += 1
        coin = random.random() #Return a random integer N such that a <= N <= b. 
        if coin>0.5:
            hcount += 1
        else:
            tcount += 1
    phead = hcount/ flips*100
    ptail = 100-phead
    print("Total no of flips",flips)
    print("percentage of head",phead)
    print("percentage of tail",ptail)
tries = int(input("enter tries:"))
fun(tries)