fruits = ['grape', 'banana', 'strawberry', 'apple', 'peach', 'cherry']
for j in range(len(fruits)-1,0,-1):
    for i in range(j):
        if fruits[i]>fruits[i+1]:
            fruits[i],fruits[i+1]=fruits[i+1],fruits[i]
print(fruits)