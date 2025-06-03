n=int(input())
a=list(map(int,input().split()))
l=0
r=sum(a)
ans=20202020200

for i in range(n):
  l+=a[i]
  r-=a[i]
  ans=min(ans,abs(l-r))
  
print(ans)