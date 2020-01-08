m ,n = [int(m) for m in input("enter row and colum number:").split()]
arr = [[int(input("enter [{0}][{1}] value:".format(x,y))) for x in range (m)] for y in range(n)]
# print(arr) o/p[[0,0,0],[0,0,0]]
for rows in arr:
    print(rows)
