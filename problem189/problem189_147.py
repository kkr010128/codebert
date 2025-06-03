def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n,m=sep()
k=(n*(n-1))//2
k=k+ (m*(m-1))//2
print(k)