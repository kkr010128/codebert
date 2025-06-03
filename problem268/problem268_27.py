n=int(input())
a=list(map(int,input().split()))

l=[0,0,0]

mod=10**9+7

ans=1
for i in a:
  ans*=l.count(i)
  ans%=mod
  for j in range(3):
    if l[j]==i:
      l[j]+=1
      break

print(ans)