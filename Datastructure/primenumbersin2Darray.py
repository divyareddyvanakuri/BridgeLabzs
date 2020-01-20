mylist = []
lower = 0
upper = 1000
for number in range(lower,upper):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
           mylist.append(number)
#print(mylist)

A = [[x for x in range(100) if x in mylist],[x for x in range(100,200) if x in mylist],
    [x for x in range(200,300) if x in mylist],[x for x in range(300,400) if x in mylist],
    [x for x in range(400,500) if x in mylist],[x for x in range(500,600) if x in mylist],
    [x for x in range(600,700) if x in mylist],[x for x in range(800,900) if x in mylist],
    [x for x in range(900,1000) if x in mylist]]
print(A)
