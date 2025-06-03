n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
d=[-1,-1,-1]
ans=1
for aa in a:
  ans*=d.count(aa-1)
  ans%=mod
  if aa-1 in d:
    d[d.index(aa-1)]+=1
print(ans)
