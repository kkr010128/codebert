n,k,s=map(int,input().split())
a=[1 for i in range(n)]
for i in range(k):
    a[i]=s
for i in range(k,n):
    if s!=10**9:
        a[i]+=s
    else:
        a[i]=1
if k==0:
    if s!=10**9:
        a=[10**9 for i in range(n)]
    else:
        a=[1 for i in range(n)]
      
print(*a)