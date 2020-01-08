def distincttriplets(a,n):
    count = 0
    for i in  range(n):
        for j in range(i+1,n):
            for k in range(i+2,n):
                if a[i]+a[j]+a[k]==0:
                    print("distinct triplets:",a[i],a[j],a[k]) 
                    count += 1
    print("number of distinct triplets:",count)
num = int(input("enter list range:"))
a = [int(input("enter list {0} value:".format(i))) for i in range(num)]
n = len(a)
distincttriplets(a,n)                    