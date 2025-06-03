n = int(input())
a = list(map(int, input().split()))
from collections import Counter
c = Counter(a)
vals = [True]*(max(a)+1)
ans = 0
m = max(a)+1
for i in range(1, m):
    if i not in c:
        continue
    if c[i]>=2:
        vals[i] = False
    for j in range(2*i, m, i):
        vals[j] = False
ans = 0
for i in range(1, max(a)+1):
  if vals[i] and i in c:
    ans += 1

print(ans)