def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
ar=lis()
k=0
for i in ar:
    k=(k^i)
for i in ar:
    print(k^i,end=" ")
