from collections import defaultdict
from itertools import accumulate
n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0] + list(accumulate(A))
Q = [ (S[i]-i)%k for i in range(n+1) ]
d = defaultdict(int)
ans = 0
for j in range(n):
  d[Q[j]] += 1
  if j-k+1 >= 0:
    d[Q[j-k+1]] -= 1
  ans += d[Q[j+1]]
print(ans)