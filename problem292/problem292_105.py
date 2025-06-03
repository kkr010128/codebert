from itertools import combinations

n=int(input())
D=list(map(int,input().split()))

ans=0
for a,b in combinations(range(n),2):
  ans+=D[a]*D[b]
  
print(ans)