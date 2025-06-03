n,k,s=map(int,input().split())
a=[s]*(k)
for i in range(n-k):
    a.append(max((s+1)%(10**9),1))
b=[]
for i in range(n):
    b.append(str(a[i]))
print(" ".join(b))
