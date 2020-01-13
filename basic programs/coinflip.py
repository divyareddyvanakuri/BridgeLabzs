import random
def coinflips(tries):
    hcount = 0
    tcount = 0
    flips = 0
    while flips<tries:
        flips += 1
        coin = random.random()  # Random float:  0.0 <= x < 1.0
        if coin>0.5:
            hcount += 1
        else:
            tcount += 1
    phead = round(hcount/ flips*100,3)
    ptail = 100-phead
    print("percentage of head:",phead)
    print("percentage of tail:",ptail)
tries = int(input("enter tries:"))
coinflips(tries)