n,k=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(min(k,41)):
  b=[0]*(n+1)
  for i in range(n):
    l=max(0,i-a[i])
    r=min(n,i+a[i]+1)
    b[l]+=1
    b[r]-=1
  for i in range(n-1):
    b[i+1]+=b[i]
  a=b[:n]
print(*a)