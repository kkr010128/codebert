from itertools import combinations
n,m,x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

ans = float("inf")
for i in range(1,n+1):
  for j in combinations(ca,i):
    l = [0]*(m+1)
    for k in j:
      for i2 in range(m+1):
        l[i2] += k[i2]
    if all(l[num] >= x for num in range(1,m+1)):
      ans = min(ans, l[0])
if ans == float("inf"): print(-1)
else: print(ans)