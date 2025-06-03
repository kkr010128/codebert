n=int(input())
d=list(map(int,input().split()))
l=[x for x in range(n)]


import itertools

p=list(itertools.combinations(l,2))

ans=0

for pp in p:
  ans+=d[pp[0]]*d[pp[1]]

print(ans)