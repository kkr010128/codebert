n,k,*a=map(int,open(0).read().split())
def f(b):
    rt=[0]*-~n
    for i in range(n):
        d=b[i]
        rt[max(0,i-d)]+=1
        rt[min(n,i+d+1)]+=-1
    for i in range(n-1):
        rt[i+1]+=rt[i]
    return rt[:-1]

for i in range(k):
    a=f(a)
    if sum(a)==n**2:
        break
print(*a)
