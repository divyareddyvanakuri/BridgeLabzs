nodes = int(input("number of nodes in a binary tree:"))
k = 2*nodes
j = nodes+1
def factorial(number):
    Factorial = 1
    for i in range(1,number+1):
       Factorial *= i
    return Factorial
def Noofbinartsearchtrees():
    numerator = factorial(k)
    denomenator_var1 = factorial(j)
    denomenator_var2 = factorial(nodes)
    catalan_number = int(numerator/(denomenator_var1*denomenator_var2))
    return catalan_number
cn = Noofbinartsearchtrees()
print("Count of binary trees with {0} nodes is {1}".format(nodes,cn))
