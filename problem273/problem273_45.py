import collections
n,k=map(int,input().split())
a=list(map(int,input().split()))
m=[0]
for i in range(n):
  m.append((m[-1]+a[i]))
for i in range(n+1):
  m[i]-=i
  m[i]%=k

ans=0
dict=collections.defaultdict(int)
for i in range(1,n+1):
  x=m[i]
  if i<=k-1:
    dict[m[i-1]]+=1
  else:
    dict[m[i-1]]+=1
    dict[m[i-k]]-=1
  ans+=dict[x]
print(ans)