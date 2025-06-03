n,*a=map(int,open(0).read().split())
l=[a[0]]*n
for i in range(1,n):
  l[i]=l[i-1]+a[i]
r=[l[-1]]*n
for i in range(1,n):
  r[i]=r[i-1]-a[i-1]
ans=10**20
for i in range(n-1):
  ans=min(abs(l[i]-r[i+1]),ans)
print(ans)