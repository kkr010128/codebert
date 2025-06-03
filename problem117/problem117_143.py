n,m,p=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

a=[0]*(n+1) ; b=[0]*(m+1)
for i in range(n):
    a[i+1]+=a[i]+A[i]
for j in range(m):
    b[j+1]=b[j]+B[j]
    

now=-1
import bisect as bi
for i in range(n+1):
    if a[i]>p : break
    G=p-a[i]   
    now=max(bi.bisect(b, G)+i-1, now)

print(now)
