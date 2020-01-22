print("Enter range between 0-1000")
lower = int(input("enter lower range value:"))
upper = int(input("enter higher range value:"))

def primeanagrams(lower,upper):
    prime_list=[]
    for val in range(lower,upper+1):
        if val>1:
            for n in range(2,val):
                if (val%n) == 0:
                    break
            else:
                prime_list.append(val)
    anagram_list=[]
    for i in prime_list:
        for j in prime_list:
            if i != j and sorted(str(i))==sorted(str(j)):
                anagram_list.append(j) 
    return anagram_list 
if lower > upper:
    print("Ensure Entered lower range value needs to be less the Entered higher range value")
else:
    mylist=primeanagrams(lower,upper)
    TwoDArray_anagramprime = [[x for x in range(100) if x in mylist],[x for x in range(100,200) if x in mylist],
        [x for x in range(200,300) if x in mylist],[x for x in range(300,400) if x in mylist],
        [x for x in range(400,500) if x in mylist],[x for x in range(500,600) if x in mylist],
        [x for x in range(600,700) if x in mylist],[x for x in range(800,900) if x in mylist],
        [x for x in range(900,1000) if x in mylist]]
    print(TwoDArray_anagramprime)