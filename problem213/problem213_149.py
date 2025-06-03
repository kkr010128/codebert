n=int(input())
x=list(map(int,input().split()))
x.sort()
m=10000000000
for i in range(x[0],x[n-1]+1):
  ans=0
  for j in range(n):
    ans+=(i-x[j])**2
  m=min(m,ans)

print(m)