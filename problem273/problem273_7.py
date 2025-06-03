from collections import defaultdict
from bisect import bisect_left
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    a[i] -= 1
for i in range(n):
    a[i + 1] += a[i]
    a[i] %= k
a[i + 1] %= k
c = defaultdict(list)
for i in range(n + 1):
    c[a[i]].append(i)
ans = 0
for v in c.values():
    for i in range(len(v)):
        ans += bisect_left(v, v[i] + k) - i - 1
print(ans)
