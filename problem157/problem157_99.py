N = int(input())
A = [int(i) for i in input().split()]

L = [A[i]+i+1 for i in range(N)]
R = [i + 1 - A[i] for i in range(N)]
from collections import defaultdict
l = defaultdict(int)
for i in L:
  l[i] += 1
ans = 0
for r in R:
  ans += l.get(r, 0)
print(ans)