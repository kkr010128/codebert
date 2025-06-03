n=int(input())
a=list(map(int,input().split()))
ans=float('inf')
s=sum(a)
res=0
for i in range(n):
  res+=a[i]
  s-=a[i]
  ans=min(ans,abs(s-res))
print(ans)