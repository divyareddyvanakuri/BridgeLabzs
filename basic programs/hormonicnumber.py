num = int(input("enter a harmonic number: "))
harmonic = 1
for i in range(2,num+1):
    harmonic += 1/i
print("{0}th harmonic value:{1} ".format(num,harmonic))