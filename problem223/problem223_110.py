n,k=map(int,input().split())
p=list(map(int,input().split()))
a=[0]*n
b=[0]*n
for i in range(n):
  a[i]=(p[i]+1)/2
b[0]=a[0]
for i in range(1,n):
  b[i]=b[i-1]+a[i]
ans=b[k-1]
for i in range(1,n-k+1):
  ans=max(ans,b[i+k-1]-b[i-1])
print(ans)